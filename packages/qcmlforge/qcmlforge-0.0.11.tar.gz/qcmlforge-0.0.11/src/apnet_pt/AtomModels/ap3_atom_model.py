import torch
import torch.nn as nn
from torch_scatter import scatter
from torch_geometric.nn import MessagePassing
import numpy as np
from .. import multipole
import time
from ..atomic_datasets import (
    atomic_hirshfeld_module_dataset,
    AtomicDataLoader,
    atomic_hirshfeld_collate_update,
    qcel_mon_to_pyg_data,
    atomic_collate_update_prebatched,
    atomic_collate_update_no_target,
)

import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
import os
import gc

from .ap2_atom_model import (
    max_Z,
    unsorted_segment_sum_3d,
    DistanceLayer,
    get_distances,
)


# HIRSHFELD MODEL
class AtomHirshfeldMPNN(MessagePassing):
    def __init__(self, n_message=3, n_rbf=8, n_neuron=128, n_embed=8, r_cut=5.0):
        super().__init__(aggr="add")
        self.n_message = n_message
        self.n_rbf = n_rbf
        self.n_neuron = n_neuron
        self.n_embed = n_embed
        self.r_cut = r_cut

        # embed interatomic distances into large orthogonal basis
        self.distance_layer = DistanceLayer(n_rbf, r_cut)

        # embed atom types
        self.embed_layer = nn.Embedding(max_Z + 1, n_embed)

        # zero-th order charge guess, based solely on atom type
        self.guess_layer = nn.Embedding(max_Z + 1, 1)
        # self.guess_hirshfeldVolumeRatio = nn.Embedding(max_Z + 1, 1)
        self.guess_valenceWidth = nn.Embedding(max_Z + 1, 1)

        # update layers for hidden states
        self.charge_update_layers = nn.ModuleList()
        self.dipole_update_layers = nn.ModuleList()
        self.qpole1_update_layers = nn.ModuleList()
        self.qpole2_update_layers = nn.ModuleList()
        self.hirshfeldVolumeRatio_update_layers = nn.ModuleList()
        self.valenceWidth_update_layers = nn.ModuleList()

        # readout layers for predicting multipoles from hidden states
        self.charge_readout_layers = nn.ModuleList()
        self.dipole_readout_layers = nn.ModuleList()
        self.qpole_readout_layers = nn.ModuleList()
        self.hirshfeldVolumeRatio_readout_layers = nn.ModuleList()
        self.valenceWidth_readout_layers = nn.ModuleList()

        input_layer_size = n_embed * 4 * n_rbf + n_embed * 4 + n_rbf

        layer_nodes_hidden = [
            input_layer_size,
            n_neuron * 2,
            n_neuron,
            n_neuron // 2,
            n_embed,
        ]
        layer_nodes_readout = [
            n_embed,
            n_neuron * 2,
            n_neuron,
            n_neuron // 2,
            1,
        ]
        layer_activations = [
            nn.ReLU(),
            nn.ReLU(),
            nn.ReLU(),
            None,
        ]  # None represents a linear activation

        for i in range(n_message):
            self.charge_update_layers.append(
                self._make_layers(layer_nodes_hidden, layer_activations)
            )
            self.dipole_update_layers.append(
                self._make_layers(layer_nodes_hidden, layer_activations)
            )
            self.qpole1_update_layers.append(
                self._make_layers(layer_nodes_hidden, layer_activations)
            )
            self.qpole2_update_layers.append(
                self._make_layers(layer_nodes_hidden, layer_activations)
            )

            self.hirshfeldVolumeRatio_update_layers.append(
                self._make_layers(layer_nodes_hidden, layer_activations)
            )
            self.valenceWidth_update_layers.append(
                self._make_layers(layer_nodes_hidden, layer_activations)
            )

            self.charge_readout_layers.append(
                self._make_layers(layer_nodes_readout, layer_activations)
            )
            self.dipole_readout_layers.append(nn.Linear(n_embed, 1))
            self.qpole_readout_layers.append(nn.Linear(n_embed, 1))
            self.hirshfeldVolumeRatio_readout_layers.append(
                self._make_layers(layer_nodes_readout, layer_activations)
            )
            self.valenceWidth_readout_layers.append(
                self._make_layers(layer_nodes_readout, layer_activations)
            )

    def _make_layers(self, layer_nodes, activations):
        layers = []
        for i in range(len(layer_nodes) - 1):
            layers.append(nn.Linear(layer_nodes[i], layer_nodes[i + 1]))
            if activations[i] is not None:
                layers.append(activations[i])
        return nn.Sequential(*layers)

    def get_messages(self, h0, h, rbf, e_source, e_target):
        nedge = e_source.size(0)

        h0_source = h0.index_select(0, e_source)
        h0_target = h0.index_select(0, e_target)
        h_source = h.index_select(0, e_source)
        h_target = h.index_select(0, e_target)

        # [edges x 4 * n_embed]
        h_all = torch.cat([h0_source, h0_target, h_source, h_target], dim=-1)

        # [edges, 4 * n_embed, n_rbf]
        h_all_dot = torch.einsum("ez,er->ezr", h_all, rbf)
        # [edges, 4 * n_embed * n_rbf]
        h_all_dot = h_all_dot.view(nedge, -1)

        # [edges,  n_embed * 4 * n_rbf + n_embed * 4 + n_rbf]
        m_ij = torch.cat([h_all, h_all_dot, rbf], dim=-1)
        return m_ij

    # @torch.jit.trace
    def forward(
        self,
        x,
        edge_index,
        # edge_attr,
        R,
        molecule_ind,
        total_charge,
        natom_per_mol,
    ):
        # edge_index has shape [(e_source, e_target), n_edges]
        Z = x
        natom = Z.size(0)

        h_list_0 = [self.embed_layer(Z)]

        # Initial guesses
        charge = self.guess_layer(Z)
        # volume_ratio = self.guess_hirshfeldVolumeRatio(Z)
        volume_ratio = torch.ones(natom, 1, dtype=torch.float32, device=Z.device)
        # valence_widths = torch.ones(natom, 1, dtype=torch.float32, device=Z.device)
        valence_width = self.guess_valenceWidth(Z)

        dipole = torch.zeros(natom, 3, dtype=torch.float32, device=Z.device)
        qpole = torch.zeros(natom, 3, 3, dtype=torch.float32, device=Z.device)

        if edge_index.size(0) == 0:
            # need h_list to have the same number of dimensions as the number of message passing layers
            h_list = [h_list_0[0] for i in range(self.n_message + 1)]
            h_list = torch.stack(h_list, dim=0)
            # if we get a single atom, we should return ones for volume_ratio, valence_width
            return (
                charge.squeeze(),
                dipole,
                qpole,
                volume_ratio.squeeze(),
                volume_ratio.squeeze(),
                h_list,
            )

        # 1) Identify which molecules have more than one atom
        mol_ind = torch.where(natom_per_mol != 1)[0]
        keep_mask = (molecule_ind.unsqueeze(1) == mol_ind).any(dim=1)
        filtered_charge = charge[keep_mask]
        filtered_volume_ratio = volume_ratio[keep_mask]
        filtered_valence_width = valence_width[keep_mask]
        # Now `filtered_charge` contains only atoms from molecules that have >= 2 atoms.
        h_list = [h_list_0[0][keep_mask]]

        # Now we need to filter the edge_index to only include edges between
        # atoms in molecules with >= 2 atoms.
        e_source = edge_index[0]
        e_target = edge_index[1]
        edge_keep = keep_mask[e_source] & keep_mask[e_target]
        e_source = e_source[edge_keep]
        e_target = e_target[edge_keep]
        # shape [N], each kept atom -> new index
        idx_map = torch.cumsum(keep_mask, dim=0) - 1
        idx_map = idx_map.long()  # ensure integer
        e_source = idx_map[e_source]
        e_target = idx_map[e_target]

        R = R[keep_mask, :]

        #  [edges]
        dR, dR_xyz = get_distances(R, R, e_source, e_target)

        # [edges x 3]
        dr_unit = dR_xyz / dR.unsqueeze(1)
        rbf = self.distance_layer(dR)

        for i in range(self.n_message):
            #####################
            ### charge update ###
            #####################

            # [edges x message_embedding_dim]
            m_ij = self.get_messages(h_list[0], h_list[-1], rbf, e_source, e_target)

            # [atoms x message_embedding_dim]
            # m_i = unsorted_segment_sum_2d(m_ij, e_source, natom)
            # write unsorted_segment_sum_2d using scatter
            m_i = scatter(m_ij, e_source, dim=0, reduce="sum")

            # [atomx x hidden_dim]
            h_next = self.charge_update_layers[i](m_i)
            h_list.append(h_next)
            charge_update = self.charge_readout_layers[i](h_list[i + 1])
            filtered_charge += charge_update

            #####################
            ### dipole update ###
            #####################

            # [edges x n_embed]
            m_ij_dipole = self.dipole_update_layers[i](m_ij)
            # [edges x 3 x n_embed]
            m_ij_dipole = torch.einsum("ex,em->exm", dr_unit, m_ij_dipole)
            # [atoms x 3 x n_embed]
            m_i_dipole = unsorted_segment_sum_3d(m_ij_dipole, e_source, natom)
            # [atoms x 3 x 1]
            d_dipole = self.dipole_readout_layers[i](m_i_dipole)
            # [atoms x 3]
            d_dipole = d_dipole.view(natom, 3)
            dipole += d_dipole

            #########################
            ### quadrupole update ###
            #########################

            # [edges x n_embed]
            m_ij_qpole1 = self.qpole1_update_layers[i](m_ij)
            # [edges x 3 x n_embed]
            m_ij_qpole1 = torch.einsum("ex,em->exm", dr_unit, m_ij_qpole1)
            # [atoms x 3 x n_embed]
            m_i_qpole1 = unsorted_segment_sum_3d(m_ij_qpole1, e_source, natom)

            # [edges x n_embed]
            m_ij_qpole2 = self.qpole2_update_layers[i](m_ij)
            # [edges x 3 x n_embed]
            m_ij_qpole2 = torch.einsum("ex,em->exm", dr_unit, m_ij_qpole2)
            # [atoms x 3 x n_embed]
            m_i_qpole2 = unsorted_segment_sum_3d(m_ij_qpole2, e_source, natom)
            d_qpole = torch.einsum("axf,ayf->axyf", m_i_qpole1, m_i_qpole2)
            d_qpole = d_qpole + d_qpole.permute(0, 2, 1, 3)
            # Paper states 0.5 factor is applied to the sum
            # d_qpole = 0.5 * (d_qpole + d_qpole.permute(0, 2, 1, 3))
            d_qpole = self.qpole_readout_layers[i](d_qpole)
            d_qpole = d_qpole.view(natom, 3, 3)
            qpole += d_qpole

            #####################################
            ### hirshfeld volume ratio update ###
            #####################################

            # [edges x message_embedding_dim]
            m_ij_hirshfeldVolumeRatio = self.hirshfeldVolumeRatio_update_layers[i](m_i)
            filtered_volume_ratio += self.hirshfeldVolumeRatio_readout_layers[i](
                m_ij_hirshfeldVolumeRatio
            )

            ############################
            ### valence width update ###
            ############################

            m_ij_valenceWidth = self.valenceWidth_update_layers[i](m_i)
            filtered_valence_width += self.valenceWidth_readout_layers[i](
                m_ij_valenceWidth
            )

        ####################################
        ### enforce traceless quadrupole ###
        ####################################

        qpole = multipole.ensure_traceless_qpole(qpole)

        ###################################
        ### enforce charge conservation ###
        ###################################

        charge[keep_mask] = filtered_charge
        molecule_ind.requires_grad_(False)
        molecule_ind = molecule_ind.long()
        total_charge_pred = scatter(charge, molecule_ind, dim=0, reduce="sum")
        # return charge, dipole, qpole, h_list

        total_charge_pred = total_charge_pred.squeeze()
        total_charge_err = total_charge_pred - total_charge
        charge_err = torch.repeat_interleave(
            total_charge_err / natom_per_mol.float(), natom_per_mol
        ).unsqueeze(1)
        charge = charge - charge_err
        charge = charge.squeeze()
        h_list = torch.stack(h_list, dim=0)
        volume_ratio[keep_mask] = filtered_volume_ratio
        volume_ratio = volume_ratio.squeeze()
        valence_width[keep_mask] = filtered_valence_width
        valence_width = valence_width.squeeze()
        return charge, dipole, qpole, volume_ratio, valence_width, h_list


def unwrap_model(model):
    return model.module if isinstance(model, DDP) else model


def isolate_atomic_property_predictions(batch, output):
    batch_size = batch.natom_per_mol.size(0)
    qA = output[0]
    muA = output[1]
    thA = output[2]
    hfvrA = output[3]
    vwA = output[4]
    hlistA = output[5]
    mol_charges = [[] for i in range(batch_size)]
    mol_dipoles = [[] for i in range(batch_size)]
    mol_qpoles = [[] for i in range(batch_size)]
    mol_hfvr = [[] for i in range(batch_size)]
    mol_vw = [[] for i in range(batch_size)]
    mol_hlist = [[] for i in range(batch_size)]
    i_offset = 0
    for n, i in enumerate(batch.natom_per_mol):
        mol_charges[n] = qA[i_offset : i_offset + i]
        mol_dipoles[n] = muA[i_offset : i_offset + i]
        mol_qpoles[n] = thA[i_offset : i_offset + i]
        mol_hfvr[n] = hfvrA[i_offset : i_offset + i]
        mol_vw[n] = vwA[i_offset : i_offset + i]
        mol_hlist[n] = hlistA[i_offset : i_offset + i]
        i_offset += i
    return mol_charges, mol_dipoles, mol_qpoles, mol_hfvr, mol_vw, mol_hlist


class AtomHirshfeldModel:
    def __init__(
        self,
        dataset=None,
        pre_trained_model_path=None,
        n_message=3,
        n_rbf=8,
        n_neuron=128,
        n_embed=8,
        r_cut=5.0,
        use_GPU=None,
        ignore_database_null=True,
        ds_spec_type=1,
        ds_root="data_dir",
        ds_max_size=None,
        ds_batch_size=16,
        ds_testing=False,
        ds_force_reprocess=False,
        ds_in_memory=True,
        model_save_path=None,
    ):
        """
        If pre_trained_model_path is provided, the model will be loaded from
        the path and all other parameters will be ignored except for dataset.

        use_GPU will check for a GPU and use it if available unless set to false.
        """
        if torch.cuda.is_available() and use_GPU is not False:
            device = torch.device("cuda:0")
            print("running on the GPU")
        else:
            device = torch.device("cpu")
            print("running on the CPU")

        if pre_trained_model_path:
            # print(f"Loading pre-trained AtomHirshfeldMPNN model from {pre_trained_model_path}")
            checkpoint = torch.load(pre_trained_model_path, weights_only=False)
            self.model = AtomHirshfeldMPNN(
                n_message=checkpoint["config"]["n_message"],
                n_rbf=checkpoint["config"]["n_rbf"],
                n_neuron=checkpoint["config"]["n_neuron"],
                n_embed=checkpoint["config"]["n_embed"],
                r_cut=checkpoint["config"]["r_cut"],
            )
            model_state_dict = {
                k.replace("_orig_mod.", ""): v
                for k, v in checkpoint["model_state_dict"].items()
            }
            self.model.load_state_dict(model_state_dict)
        else:
            self.model = AtomHirshfeldMPNN(
                n_message=n_message,
                n_rbf=n_rbf,
                n_neuron=n_neuron,
                n_embed=n_embed,
                r_cut=r_cut,
            )
        # self.model.to(device)
        self.device = device
        self.dataset = dataset
        mp.set_sharing_strategy("file_system")
        if not ignore_database_null and self.dataset is None:
            self.dataset = atomic_hirshfeld_module_dataset(
                root=ds_root,
                testing=ds_testing,
                spec_type=ds_spec_type,
                max_size=ds_max_size,
                force_reprocess=ds_force_reprocess,
                in_memory=ds_in_memory,
                batch_size=ds_batch_size,
            )
        # print(f"{self.dataset = }")
        self.rank = None
        self.world_size = None
        self.model_save_path = model_save_path
        self.train_shuffle = None
        # torch.jit.enable_onednn_fusion(True)
        return

    def set_pretrained_model(self, model_path):
        checkpoint = torch.load(model_path)
        if "_orig_mod" not in list(self.model.state_dict().keys())[0]:
            model_state_dict = {
                k.replace("_orig_mod.", ""): v
                for k, v in checkpoint["model_state_dict"].items()
            }
            self.model.load_state_dict(model_state_dict)
        else:
            self.model.load_state_dict(checkpoint["model_state_dict"])
        return

    def compile_model(self):
        torch._dynamo.config.dynamic_shapes = True
        torch._dynamo.config.capture_dynamic_output_shape_ops = True
        torch._dynamo.config.capture_scalar_outputs = True
        self.model = torch.compile(self.model, dynamic=True)
        return

    def setup(self, rank, world_size):
        os.environ["MASTER_ADDR"] = "localhost"
        os.environ["MASTER_PORT"] = "12355"
        dist.init_process_group("gloo", rank=rank, world_size=world_size)
        # torch.manual_seed(42)

    def cleanup(self):
        dist.destroy_process_group()

    def eval_fn(self, batch):
        charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, hlist = (
            self.model(
                batch.x,
                batch.edge_index,
                # batch.edge_attr,
                R=batch.R,
                molecule_ind=batch.molecule_ind,
                total_charge=batch.total_charge,
                natom_per_mol=batch.natom_per_mol,
            )
        )
        return charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, hlist

    def evaluate_model_collate_train(self, data_loader, optimizer=None, loss_fn=None):
        charge_errors_t, dipole_errors_t, qpole_errors_t = [], [], []
        total_loss = 0.0
        self.model.train()
        for batch in data_loader:
            batch_loss = 0.0
            batch = batch.to(self.device)
            optimizer.zero_grad()
            charge, dipole, qpole, _ = self.model(
                batch.x,
                batch.edge_index,
                # batch.edge_attr,
                R=batch.R,
                molecule_ind=batch.molecule_ind,
                total_charge=batch.total_charge,
            )

            # Errors
            q_error = charge - batch.charges
            d_error = dipole - batch.dipoles
            qp_error = qpole - batch.quadrupoles
            if loss_fn is None:
                # perform mean squared error
                charge_loss = torch.mean(torch.square(q_error))
                dipole_loss = torch.mean(torch.square(d_error))
                qpole_loss = torch.mean(torch.square(qp_error))
            else:
                # perform custom loss function, or pytorch criterion loss_fn
                charge_loss = loss_fn(charge, batch.charges)
                dipole_loss = torch.mean(loss_fn(dipole, batch.dipoles))
                qpole_loss = torch.mean(loss_fn(qpole, batch.quadrupoles))

            batch_loss = charge_loss + dipole_loss + qpole_loss
            batch_loss.backward()
            optimizer.step()
            total_loss += batch_loss.detach().item()

            charge_errors_t.append(q_error.detach())
            dipole_errors_t.extend(d_error.detach())
            qpole_errors_t.extend(qp_error.detach())
        charge_errors_t = torch.cat(charge_errors_t)
        dipole_errors_t = torch.cat(dipole_errors_t)
        qpole_errors_t = torch.cat(qpole_errors_t)
        return total_loss, charge_errors_t, dipole_errors_t, qpole_errors_t

    def evaluate_model_collate_eval(self, data_loader, loss_fn=None):
        charge_errors_t, dipole_errors_t, qpole_errors_t, hfvr_errors_t, vw_errors_t = (
            [],
            [],
            [],
            [],
            [],
        )
        total_loss = 0.0
        self.model.eval()
        with torch.no_grad():
            for batch in data_loader:
                batch_loss = 0.0
                batch = batch.to(self.device)
                (
                    charge,
                    dipole,
                    qpole,
                    hirshfeld_volume_ratios,
                    valence_widths,
                    hlist,
                ) = self.model(
                    batch.x,
                    batch.edge_index,
                    # batch.edge_attr,
                    R=batch.R,
                    molecule_ind=batch.molecule_ind,
                    total_charge=batch.total_charge,
                    natom_per_mol=batch.natom_per_mol,
                )

                # Errors
                q_error = charge - batch.charges
                d_error = dipole - batch.dipoles
                qp_error = qpole - batch.quadrupoles
                hfvr_error = hirshfeld_volume_ratios - batch.volume_ratios
                vw_error = valence_widths - batch.valence_widths
                if loss_fn is None:
                    # perform mean squared error
                    charge_loss = torch.mean(torch.square(q_error))
                    dipole_loss = torch.mean(torch.square(d_error))
                    qpole_loss = torch.mean(torch.square(qp_error))
                    hfvr_loss = torch.mean(torch.square(hfvr_error))
                    vw_loss = torch.mean(torch.square(vw_error))
                else:
                    # perform custom loss function, or pytorch criterion loss_fn
                    charge_loss = loss_fn(charge, batch.charges)
                    dipole_loss = torch.mean(loss_fn(dipole, batch.dipoles))
                    qpole_loss = torch.mean(loss_fn(qpole, batch.quadrupoles))
                    hfvr_loss = torch.mean(
                        loss_fn(hirshfeld_volume_ratios, batch.volume_ratios)
                    )
                    vw_loss = torch.mean(loss_fn(valence_widths, batch.valence_widths))

                batch_loss = (
                    charge_loss + dipole_loss + qpole_loss + hfvr_loss + vw_loss
                )
                total_loss += batch_loss.detach()

            charge_errors_t.append(q_error.detach())
            dipole_errors_t.extend(d_error.detach())
            qpole_errors_t.extend(qp_error.detach())
            hfvr_errors_t.extend(hfvr_error.detach())
            vw_errors_t.extend(vw_error.detach())
        charge_errors_t = torch.cat(charge_errors_t)
        dipole_errors_t = torch.cat(dipole_errors_t)
        qpole_errors_t = torch.cat(qpole_errors_t)
        hfvr_errors_t = torch.cat(hfvr_errors_t)
        vw_errors_t = torch.cat(vw_errors_t)
        return (
            total_loss,
            charge_errors_t,
            dipole_errors_t,
            qpole_errors_t,
            hfvr_errors_t,
            vw_errors_t,
        )

    def pretrain_statistics(self, train_loader, test_loader, criterion):
        t1 = time.time()
        with torch.no_grad():
            (
                _,
                charge_errors_t,
                dipole_errors_t,
                qpole_errors_t,
                hfvr_errors_t,
                vw_errors_t,
            ) = self.evaluate_model_collate_eval(
                train_loader,  # loss_fn=criterion
            )
            charge_MAE_t = np.mean(np.abs(charge_errors_t))
            dipole_MAE_t = np.mean(np.abs(dipole_errors_t))
            qpole_MAE_t = np.mean(np.abs(qpole_errors_t))
            hfvr_MAE_t = np.mean(np.abs(hfvr_errors_t))
            vw_MAE_t = np.mean(np.abs(vw_errors_t))

            (
                charge_errors_t,
                dipole_errors_t,
                qpole_errors_t,
                hfvr_errors_t,
                vw_errors_t,
            ) = [], [], [], []
            (
                test_loss,
                charge_errors_v,
                dipole_errors_v,
                qpole_errors_v,
                hfvr_errors_v,
                vw_errors_v,
            ) = self.evaluate_model_collate_eval(
                test_loader,  # loss_fn=criterion
            )
            charge_MAE_v = np.mean(np.abs(charge_errors_v))
            dipole_MAE_v = np.mean(np.abs(dipole_errors_v))
            qpole_MAE_v = np.mean(np.abs(qpole_errors_v))
            hfvr_MAE_v = np.mean(np.abs(hfvr_errors_v))
            vw_MAE_v = np.mean(np.abs(vw_errors_v))
            (
                charge_errors_v,
                dipole_errors_v,
                qpole_errors_v,
                hfvr_errors_v,
                vw_errors_v,
            ) = [], [], [], [], []
            dt = time.time() - t1
            print(
                f"  (Pre-training) ({dt:<7.2f} sec)  MAE: {charge_MAE_t:>7.4f}/{charge_MAE_v:<7.4f} {dipole_MAE_t:>7.4f}/{dipole_MAE_v:<7.4f} {qpole_MAE_t:>7.4f}/{qpole_MAE_v:<7.4f} {hfvr_MAE_t:>7.4f}/{hfvr_MAE_v:<7.4f} {vw_MAE_t:>7.4f}/{vw_MAE_v:<7.4f}",
                flush=True,
            )
        return test_loss

    def train_batches_single_proc(
        self, rank, dataloader, criterion, optimizer, rank_device
    ):
        self.model.train()
        total_charge_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_dipole_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_qpole_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_hfvr_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_vw_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_loss = 0.0

        total_count = torch.zeros([], dtype=torch.int, device=rank_device)

        for batch in dataloader:
            batch = batch.to(rank_device, non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, _ = (
                self.eval_fn(batch)
            )

            q_error = charge - batch.charges
            d_error = dipole - batch.dipoles
            qp_error = qpole - batch.quadrupoles
            hfvr_error = hirshfeld_volume_ratios - batch.volume_ratios
            vw_error = valence_widths - batch.valence_widths

            charge_loss = (q_error**2).mean()
            dipole_loss = (d_error**2).mean()
            qpole_loss = (qp_error**2).mean()
            hfvr_loss = (hfvr_error**2).mean()
            vw_loss = (vw_error**2).mean()

            loss = charge_loss + dipole_loss + qpole_loss + hfvr_loss + vw_loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            total_count += q_error.numel()

            total_charge_error += q_error.detach().abs().sum()
            total_dipole_error += d_error.detach().abs().sum()
            total_qpole_error += qp_error.detach().abs().sum()
            total_hfvr_error += hfvr_error.detach().abs().sum()
            total_vw_error += vw_error.detach().abs().sum()

        final_count = total_count.item()

        # Calculating MAEs
        charge_mae = total_charge_error.item() / final_count
        dipole_mae = total_dipole_error.item() / (final_count * 3)
        qpole_mae = total_qpole_error.item() / (final_count * 9)
        hfvr_mae = total_hfvr_error.item() / final_count
        vw_mae = total_vw_error.item() / final_count
        return total_loss, charge_mae, dipole_mae, qpole_mae, hfvr_mae, vw_mae

    def train_batches(self, rank, dataloader, criterion, optimizer, rank_device):
        self.model.train()
        total_charge_error = 0
        total_dipole_error = 0
        total_qpole_error = 0
        total_hfvr_error = 0
        total_vw_error = 0
        total_loss = 0
        count = 0

        for batch in dataloader:
            batch = batch.to(rank_device)
            optimizer.zero_grad()
            charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, _ = (
                self.eval_fn(batch)
            )

            q_error = charge - batch.charges
            d_error = dipole - batch.dipoles
            qp_error = qpole - batch.quadrupoles
            hfvr_error = hirshfeld_volume_ratios - batch.volume_ratios
            vw_error = valence_widths - batch.valence_widths

            charge_loss = torch.mean(torch.square(q_error))
            dipole_loss = torch.mean(torch.square(d_error))
            qpole_loss = torch.mean(torch.square(qp_error))
            hfvr_loss = torch.mean(torch.square(hfvr_error))
            vw_loss = torch.mean(torch.square(vw_error))

            loss = charge_loss + dipole_loss + qpole_loss + hfvr_loss + vw_loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            count += q_error.numel()

            total_charge_error += torch.sum(torch.abs(q_error)).item()
            total_dipole_error += torch.sum(torch.abs(d_error)).item()
            total_qpole_error += torch.sum(torch.abs(qp_error)).item()
            total_hfvr_error += torch.sum(torch.abs(hfvr_error)).item()
            total_vw_error += torch.sum(torch.abs(vw_error)).item()

        # Converting to tensors for all-reduce
        total_charge_error = torch.tensor(
            total_charge_error, dtype=torch.float32, device=rank_device
        )
        total_dipole_error = torch.tensor(
            total_dipole_error, dtype=torch.float32, device=rank_device
        )
        total_qpole_error = torch.tensor(
            total_qpole_error, dtype=torch.float32, device=rank_device
        )
        total_hfvr_error = torch.tensor(
            total_hfvr_error, dtype=torch.float32, device=rank_device
        )
        total_vw_error = torch.tensor(
            total_vw_error, dtype=torch.float32, device=rank_device
        )
        count = torch.tensor(count, dtype=torch.int, device=rank_device)

        # All-reduce across processes
        dist.all_reduce(total_charge_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_dipole_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_qpole_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_hfvr_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_vw_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(count, op=dist.ReduceOp.SUM)

        # Calculating MAEs
        charge_mae = total_charge_error.item() / count.item()
        dipole_mae = total_dipole_error.item() / (count.item() * 3)
        qpole_mae = total_qpole_error.item() / (count.item() * 9)
        hfvr_mae = total_hfvr_error.item() / count.item()
        vw_mae = total_vw_error.item() / count.item()

        return total_loss, charge_mae, dipole_mae, qpole_mae, hfvr_mae, vw_mae

    def evaluate_batches_single_proc(self, rank, dataloader, criterion, rank_device):
        self.model.eval()
        total_charge_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_dipole_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_qpole_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_hfvr_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_vw_error = torch.zeros([], dtype=torch.float32, device=rank_device)
        total_loss = 0.0

        total_count = torch.zeros([], dtype=torch.int, device=rank_device)

        with torch.no_grad():
            for batch in dataloader:
                batch = batch.to(rank_device, non_blocking=True)
                charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, _ = (
                    self.eval_fn(batch)
                )

                q_error = charge - batch.charges
                d_error = dipole - batch.dipoles
                qp_error = qpole - batch.quadrupoles
                hfvr_error = hirshfeld_volume_ratios - batch.volume_ratios
                vw_error = valence_widths - batch.valence_widths

                charge_loss = (q_error**2).mean()
                dipole_loss = (d_error**2).mean()
                qpole_loss = (qp_error**2).mean()
                hfvr_loss = (hfvr_error**2).mean()
                vw_loss = (vw_error**2).mean()

                loss = charge_loss + dipole_loss + qpole_loss + hfvr_loss + vw_loss
                total_loss += loss.item()
                total_count += q_error.numel()

                total_charge_error += q_error.abs().sum()
                total_dipole_error += d_error.abs().sum()
                total_qpole_error += qp_error.abs().sum()
                total_hfvr_error += hfvr_error.abs().sum()
                total_vw_error += vw_error.abs().sum()

        final_count = total_count.item()

        # Calculating MAEs
        charge_mae = total_charge_error.item() / final_count
        dipole_mae = total_dipole_error.item() / (final_count * 3)
        qpole_mae = total_qpole_error.item() / (final_count * 9)
        hfvr_mae = total_hfvr_error.item() / final_count
        vw_mae = total_vw_error.item() / final_count
        return total_loss, charge_mae, dipole_mae, qpole_mae, hfvr_mae, vw_mae

    def evaluate_batches(self, rank, dataloader, criterion, rank_device):
        self.model.eval()
        total_charge_error = 0
        total_dipole_error = 0
        total_qpole_error = 0
        total_hfvr_error = 0
        total_vw_error = 0
        total_loss = 0
        count = 0

        with torch.no_grad():
            for batch in dataloader:
                batch = batch.to(rank_device)
                charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, _ = (
                    self.eval_fn(batch)
                )

                q_error = charge - batch.charges
                d_error = dipole - batch.dipoles
                qp_error = qpole - batch.quadrupoles
                hfvr_error = hirshfeld_volume_ratios - batch.volume_ratios
                vw_error = valence_widths - batch.valence_widths

                total_charge_error += torch.sum(torch.abs(q_error)).item()
                total_dipole_error += torch.sum(torch.abs(d_error)).item()
                total_qpole_error += torch.sum(torch.abs(qp_error)).item()
                total_hfvr_error += torch.sum(torch.abs(hfvr_error)).item()
                total_vw_error += torch.sum(torch.abs(vw_error)).item()

                charge_loss = torch.mean(torch.square(q_error))
                dipole_loss = torch.mean(torch.square(d_error))
                qpole_loss = torch.mean(torch.square(qp_error))
                hfvr_loss = torch.mean(torch.square(hfvr_error))
                vw_loss = torch.mean(torch.square(vw_error))

                total_loss += (
                    charge_loss + dipole_loss + qpole_loss + hfvr_loss + vw_loss
                )
                count += q_error.numel()

        # Converting to tensors for all-reduce
        total_charge_error = torch.tensor(
            total_charge_error, dtype=torch.float32, device=rank_device
        )
        total_dipole_error = torch.tensor(
            total_dipole_error, dtype=torch.float32, device=rank_device
        )
        total_qpole_error = torch.tensor(
            total_qpole_error, dtype=torch.float32, device=rank_device
        )
        total_hfvr_error = torch.tensor(
            total_hfvr_error, dtype=torch.float32, device=rank_device
        )
        total_vw_error = torch.tensor(
            total_vw_error, dtype=torch.float32, device=rank_device
        )
        count = torch.tensor(count, dtype=torch.int, device=rank_device)

        # All-reduce across processes
        dist.all_reduce(total_charge_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_dipole_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_qpole_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_hfvr_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(total_vw_error, op=dist.ReduceOp.SUM)
        dist.all_reduce(count, op=dist.ReduceOp.SUM)

        total_loss = torch.tensor(total_loss.item(), device=rank_device)
        dist.all_reduce(total_loss, op=dist.ReduceOp.SUM)

        # Calculating MAEs
        charge_mae = total_charge_error.item() / count.item()
        dipole_mae = total_dipole_error.item() / (count.item() * 3)
        qpole_mae = total_qpole_error.item() / (count.item() * 9)
        hfvr_mae = total_hfvr_error.item() / count.item()
        vw_mae = total_vw_error.item() / count.item()
        return total_loss, charge_mae, dipole_mae, qpole_mae, hfvr_mae, vw_mae

    def ddp_train(
        self,
        rank,
        world_size,
        train_dataset,
        test_dataset,
        n_epochs,
        batch_size,
        lr,
        pin_memory,
        num_workers,
    ):
        # print(f"{self.device.type = }")
        if self.device.type == "cpu":
            # rank = "cpu"
            rank_device = "cpu"
        else:
            rank_device = rank
        if world_size > 1:
            self.setup(rank, world_size)

        self.model.to(rank_device)
        if world_size > 1 and rank_device == "cpu":
            torch._dynamo.config.dynamic_shapes = True
            torch._dynamo.config.capture_dynamic_output_shape_ops = True
            torch._dynamo.config.capture_scalar_outputs = True
            self.model = torch.compile(self.model, dynamic=True)
            self.model = DDP(
                self.model,
            )
        # elif rank_device != "cpu":
        #     self.model = DDP(
        #         self.model,
        #         device_ids=[rank],
        #         output_device=rank_device,
        #     )

        train_sampler = (
            torch.utils.data.distributed.DistributedSampler(
                train_dataset, num_replicas=world_size, rank=rank
            )
            if world_size > 1
            else None
        )
        test_sampler = (
            torch.utils.data.distributed.DistributedSampler(
                test_dataset, num_replicas=world_size, rank=rank, shuffle=False
            )
            if world_size > 1
            else None
        )

        train_loader = AtomicDataLoader(
            dataset=train_dataset,
            batch_size=batch_size,
            shuffle=(train_sampler is None),
            num_workers=num_workers,
            pin_memory=pin_memory,
            sampler=train_sampler,
            collate_fn=atomic_collate_update_prebatched,
            # collate_fn=atomic_hirshfeld_collate_update,
        )

        test_loader = AtomicDataLoader(
            dataset=test_dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers,
            pin_memory=pin_memory,
            sampler=test_sampler,
            collate_fn=atomic_collate_update_prebatched,
            # collate_fn=atomic_hirshfeld_collate_update,
        )

        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        criterion = torch.nn.MSELoss()

        test_loss = self.pretrain_statistics(train_loader, test_loader, criterion)

        lowest_test_loss = test_loss

        for epoch in range(n_epochs):
            t1 = time.time()
            test_lowered = False
            train_loss, charge_MAE_t, dipole_MAE_t, qpole_MAE_t, hfvr_MAE_t = (
                self.train_batches(
                    rank, train_loader, criterion, optimizer, rank_device
                )
            )
            test_loss, charge_MAE_v, dipole_MAE_v, qpole_MAE_v, hfvr_MAE_v = (
                self.evaluate_batches(rank, test_loader, criterion, rank_device)
            )

            if rank == 0:
                if test_loss < lowest_test_loss:
                    lowest_test_loss = test_loss
                    test_lowered = "*"
                    if self.model_save_path:
                        # cpu_model = self.model.to("cpu")
                        cpu_model = unwrap_model(self.model).to("cpu")
                        torch.save(
                            {
                                "model_state_dict": cpu_model.state_dict(),
                                "config": {
                                    "n_message": cpu_model.n_message,
                                    "n_rbf": cpu_model.n_rbf,
                                    "n_neuron": cpu_model.n_neuron,
                                    "n_embed": cpu_model.n_embed,
                                    "r_cut": cpu_model.r_cut,
                                },
                            },
                            self.model_save_path,
                        )
                        self.model.to(self.device)
                else:
                    test_lowered = " "
                dt = time.time() - t1
                test_loss = 0.0
                # if (world_size==1 or rank == 0):
                print(
                    f"  EPOCH: {epoch:4d} ({dt:<7.2f} sec)     MAE: {charge_MAE_t:>7.4f}/{charge_MAE_v:<7.4f} {dipole_MAE_t:>7.4f}/{dipole_MAE_v:<7.4f} {qpole_MAE_t:>7.4f}/{qpole_MAE_v:<7.4f} {hfvr_MAE_t:>7.4f}/{hfvr_MAE_v:<7.4f} {test_lowered}",
                    flush=True,
                )
        if world_size > 1:
            self.cleanup()
        return

    def single_proc_train(
        self,
        rank,
        world_size,
        train_dataset,
        test_dataset,
        n_epochs,
        batch_size,
        lr,
        pin_memory,
        num_workers,
        skip_compile=False,
    ):
        if self.device.type == "cpu":
            rank_device = "cpu"
        else:
            rank_device = rank

        self.model.to(rank_device)
        if not skip_compile:
            self.compile_model()

        train_loader = AtomicDataLoader(
            dataset=train_dataset,
            batch_size=batch_size,
            shuffle=self.train_shuffle,
            num_workers=num_workers,
            pin_memory=pin_memory,
            collate_fn=atomic_collate_update_prebatched,
            # collate_fn=atomic_hirshfeld_collate_update,
        )

        test_loader = AtomicDataLoader(
            dataset=test_dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers,
            pin_memory=pin_memory,
            collate_fn=atomic_collate_update_prebatched,
            # collate_fn=atomic_hirshfeld_collate_update,
        )

        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        criterion = torch.nn.MSELoss()

        lowest_test_loss = torch.tensor(float("inf"))
        print(f"{rank=}")
        # self.pretrain_statistics(train_loader, test_loader, criterion)
        for epoch in range(n_epochs):
            t1 = time.time()
            test_lowered = False
            (
                train_loss,
                charge_MAE_t,
                dipole_MAE_t,
                qpole_MAE_t,
                hfvr_MAE_t,
                vw_MAE_t,
            ) = self.train_batches_single_proc(
                rank, train_loader, criterion, optimizer, rank_device
            )
            test_loss, charge_MAE_v, dipole_MAE_v, qpole_MAE_v, hfvr_MAE_v, vw_MAE_v = (
                self.evaluate_batches_single_proc(
                    rank, test_loader, criterion, rank_device
                )
            )

            if rank == 0:
                if test_loss < lowest_test_loss:
                    lowest_test_loss = test_loss
                    test_lowered = "*"
                    if self.model_save_path:
                        # cpu_model = self.model.to("cpu")
                        cpu_model = unwrap_model(self.model).to("cpu")
                        torch.save(
                            {
                                "model_state_dict": cpu_model.state_dict(),
                                "config": {
                                    "n_message": cpu_model.n_message,
                                    "n_rbf": cpu_model.n_rbf,
                                    "n_neuron": cpu_model.n_neuron,
                                    "n_embed": cpu_model.n_embed,
                                    "r_cut": cpu_model.r_cut,
                                },
                            },
                            self.model_save_path,
                        )
                        self.model.to(self.device)
                else:
                    test_lowered = " "
                dt = time.time() - t1
                test_loss = 0.0
                print(
                    f"  EPOCH: {epoch:4d} ({dt:<7.2f} sec)     MAE: {charge_MAE_t:>7.4f}/{charge_MAE_v:<7.4f} {dipole_MAE_t:>7.4f}/{dipole_MAE_v:<7.4f} {qpole_MAE_t:>7.4f}/{qpole_MAE_v:<7.4f} {hfvr_MAE_t:>7.4f}/{hfvr_MAE_v:<7.4f} {vw_MAE_t:>7.4f}/{vw_MAE_v:<7.4f} {test_lowered}",
                    flush=True,
                )

            # n = gc.collect()
            # print("    Garbage collector: collected %d objects." % n)
            # if rank_device != "cpu":
            #     torch.cuda.empty_cache()
        if world_size > 1:
            self.cleanup()
        return

    def train(
        self,
        dataset=None,
        n_epochs=500,
        batch_size=16,
        lr=5e-4,
        split_percent=0.9,
        model_path=None,
        skip_compile=True,
        shuffle=True,
        dataloader_num_workers=0,
        world_size=1,  # Default to 1 for single-core operation
        omp_num_threads_per_process=None,
        random_seed=42,
    ):
        self.model_save_path = model_path
        if self.model_save_path is not None:
            print(f"Saving model to {self.model_save_path}")
        if self.dataset is None and dataset is not None:
            self.dataset = dataset
        elif dataset is not None:
            print("Overriding self.dataset with passed dataset!")
            self.dataset = dataset
        if self.dataset is None:
            raise ValueError("No dataset provided")
        self.train_shuffle = shuffle

        np.random.seed(42)
        torch.manual_seed(42)
        random_indices = np.random.permutation(len(self.dataset))
        train_indices = random_indices[: int(len(self.dataset) * split_percent)]
        test_indices = random_indices[int(len(self.dataset) * split_percent) :]
        if random_seed:
            np.random.seed(random_seed)
            torch.manual_seed(random_seed)
            train_indices = np.random.permutation(train_indices)
        train_dataset = self.dataset[train_indices]
        test_dataset = self.dataset[test_indices]

        print("~~ Training Atom Model ~~", flush=True)
        print(
            f"    Training on {len(train_dataset)} samples, Testing on {len(test_dataset)} samples",
            flush=True,
        )
        print("\nNetwork Hyperparameters:", flush=True)
        print(f"  {self.model.n_message=}", flush=True)
        print(f"  {self.model.n_neuron=}", flush=True)
        print(f"  {self.model.n_embed=}", flush=True)
        print(f"  {self.model.n_rbf=}", flush=True)
        print(f"  {self.model.r_cut=}", flush=True)
        print("\nTraining Hyperparameters:", flush=True)
        print(f"  {n_epochs=}", flush=True)
        print(f"  {batch_size=}", flush=True)
        print(f"  {lr=}\n", flush=True)

        # pin_memory = torch.cuda.is_available()
        pin_memory = True

        if skip_compile:
            torch.jit.enable_onednn_fusion(True)
            torch.autograd.set_detect_anomaly(False)

        if world_size > 1:
            # os.environ["OMP_NUM_THREADS"] = str(dataloader_num_workers + 1)
            print("Running multi-process training", flush=True)
            os.environ["OMP_NUM_THREADS"] = str(omp_num_threads_per_process)
            mp.spawn(
                self.ddp_train,
                args=(
                    world_size,
                    train_dataset,
                    test_dataset,
                    n_epochs,
                    batch_size,
                    lr,
                    pin_memory,
                    dataloader_num_workers,
                ),
                nprocs=world_size,
                join=True,
            )
        else:
            # Run single-process training directly
            print("Running single-process training", flush=True)
            os.environ["OMP_NUM_THREADS"] = str(omp_num_threads_per_process)
            self.single_proc_train(
                rank=0,
                world_size=world_size,
                train_dataset=train_dataset,
                test_dataset=test_dataset,
                n_epochs=n_epochs,
                batch_size=batch_size,
                lr=lr,
                pin_memory=pin_memory,
                num_workers=dataloader_num_workers,
                skip_compile=skip_compile,
            )

        return

    @torch.inference_mode()
    def predict_multipoles_batch(self, batch, isolate_predictions=True):
        batch.to(self.device)
        self.model.to(self.device)
        qA, muA, thA, hfvrA, vwA, hlistA = self.model_predict(batch)
        batch = batch.cpu()
        qA = qA.detach().detach().cpu()
        muA = muA.detach().detach().cpu()
        thA = thA.detach().detach().cpu()
        hfvrA = hfvrA.detach().detach().cpu()
        vwA = vwA.detach().detach().cpu()
        hlistA = hlistA.detach().cpu()
        if isolate_predictions:
            return isolate_atomic_property_predictions(
                batch, (qA, muA, thA, hfvrA, vwA, hlistA)
            )
        else:
            return qA, muA, thA, hfvrA, vwA, hlistA

    @torch.inference_mode()
    def predict_multipoles_dataset(
        self,
        batch_size=16,
        dataloader_num_workers=0,
        world_size=1,  # Default to 1 for single-process operation
        # omp_num_threads_per_process=None,
    ):
        output = []
        data = AtomicDataLoader(self.dataset, batch_size=batch_size, shuffle=False)
        if world_size > 1:
            raise NotImplementedError(
                "Multi-process prediction not implemented yet due to needing to determine how to handle the output data merging."
            )
            # output = mp.spawn(
            #     self.predict_multipoles_dataset_process,
            #     args=(data, batch_size, dataloader_num_workers),
            #     nprocs=world_size,
            #     join=True,
            # )
        else:
            for batch in data:
                (
                    charges,
                    dipoles,
                    qpoles,
                    hirshfeld_volume_ratios,
                    valence_widths,
                    hlists,
                ) = self.model_predict(batch)
                # need to use batch.molecule_ind to reassemble the output
                mol_charges = [[] for i in range(batch_size)]
                mol_dipoles = [[] for i in range(batch_size)]
                mol_qpoles = [[] for i in range(batch_size)]
                mol_hfvr = [[] for i in range(batch_size)]
                mol_vw = [[] for i in range(batch_size)]
                for n, i in enumerate(batch.molecule_ind):
                    mol_charges[i].append(charges[n])
                    mol_dipoles[i].append(dipoles[n])
                    mol_qpoles[i].append(qpoles[n])
                    mol_hfvr[i].append(hirshfeld_volume_ratios[n])
                    mol_vw[i].append(valence_widths[n])
                output.append(
                    (mol_charges, mol_dipoles, mol_qpoles, mol_hfvr, mol_vw, hlists)
                )
        return output

    @torch.inference_mode()
    def predict_qcel_mols(self, mols, batch_size=2):
        output = []
        mol_data = []
        cnt = 0
        for mol in mols:
            data = qcel_mon_to_pyg_data(mol)
            mol_data.append(data)
            cnt += 1
            if len(mol_data) == batch_size or cnt == len(mols):
                batch = atomic_collate_update_no_target(mol_data)
                with torch.no_grad():
                    charge, dipole, qpole, hfvr, vw, hlist = self.eval_fn(batch)
                    # Isolate atomic properties by molecule
                    (
                        mol_charges,
                        mol_dipoles,
                        mol_qpoles,
                        mol_hfvrs,
                        mol_vws,
                        mol_hlists,
                    ) = isolate_atomic_property_predictions(
                        batch, (charge, dipole, qpole, hfvr, vw, hlist)
                    )
                    output.extend(
                        list(
                            zip(
                                mol_charges,
                                mol_dipoles,
                                mol_qpoles,
                                mol_hfvrs,
                                mol_vws,
                                mol_hlists,
                            )
                        )
                    )
                mol_data = []
        return output

    @torch.inference_mode()
    def model_predict(self, data):
        charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, hlist = (
            self.model(
                data.x,
                data.edge_index,
                # data.edge_attr,
                R=data.R,
                molecule_ind=data.molecule_ind,
                total_charge=data.total_charge,
                natom_per_mol=data.natom_per_mol,
            )
        )
        return charge, dipole, qpole, hirshfeld_volume_ratios, valence_widths, hlist
