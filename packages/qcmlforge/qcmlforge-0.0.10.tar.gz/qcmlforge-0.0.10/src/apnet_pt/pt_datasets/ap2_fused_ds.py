import os
import qcelemental as qcel
from typing import List, Optional, Sequence, Union
from torch_geometric.data.data import BaseData
from torch_geometric.data.datapipes import DatasetAdapter
from torch_geometric.data.on_disk_dataset import OnDiskDataset
from torch_geometric.data import Data
from torch_geometric.data import Dataset
import os.path as osp
import torch
from torch_geometric.data import download_url

from .. import util
from ..AtomModels.ap2_atom_model import AtomModel
from .. import atomic_datasets
from glob import glob
import tarfile
from time import time
import re
from pathlib import Path
from importlib import resources
from apnet_pt import constants


def qcel_dimer_to_fused_data(dimer, r_cut=5.0, r_cut_im=8.0, **kwargs):
    return dimer_fused_data(
        RA=dimer.get_fragment(0).geometry * constants.au2ang,
        ZA=dimer.get_fragment(0).atomic_numbers,
        TQA=dimer.get_fragment(0).molecular_charge,
        RB=dimer.get_fragment(1).geometry * constants.au2ang,
        ZB=dimer.get_fragment(1).atomic_numbers,
        TQB=dimer.get_fragment(1).molecular_charge,
        r_cut=r_cut,
        r_cut_im=r_cut_im,
        **kwargs,
    )


def assert_molecule_featurization_is_valid(atomic_props, dimer_ind):
    if len(atomic_props.molecule_ind) == 1:
        return True

    edge_index = atomic_props.edge_index
    atoms_with_edges = torch.cat([edge_index[0], edge_index[1]]).unique()
    keep_mask = torch.isin(
        torch.arange(
            len(atomic_props.molecule_ind), device=atomic_props.molecule_ind.device
        ),
        atoms_with_edges,
    )
    # all valid molecules will have edges
    if not keep_mask.all():
        print(
            "Molecule featurization is invalid. "
            "Some atoms in the molecule do not have edges."
            f"atomic_props:\n{atomic_props}. Skipping this data point."
        )
        torch.save(atomic_props, f"invalid_molecule_{dimer_ind}.pt")
        return False
    return True


def dimer_fused_data(
    RA,
    ZA,
    TQA,
    RB,
    ZB,
    TQB,
    dimer_ind,
    r_cut=5.0,
    r_cut_im=8.0,
    check_validity=True,
    **kwargs,
):
    atomic_props_A = atomic_datasets.create_atomic_data(ZA, RA, TQA, r_cut=r_cut)
    atomic_props_B = atomic_datasets.create_atomic_data(ZB, RB, TQB, r_cut=r_cut)
    if check_validity:
        valid = assert_molecule_featurization_is_valid(atomic_props_A, dimer_ind)
        if not valid:
            return None
        valid = assert_molecule_featurization_is_valid(atomic_props_B, dimer_ind)
        if not valid:
            return None
    e_AA_source, e_AA_target = pairwise_edges(atomic_props_A.R, r_cut)
    e_BB_source, e_BB_target = pairwise_edges(atomic_props_B.R, r_cut)
    e_ABsr_source, e_ABsr_target, e_ABlr_source, e_ABlr_target = pairwise_edges_im(
        atomic_props_A.R, atomic_props_B.R, r_cut_im
    )
    dimer_ind = torch.ones((1), dtype=torch.long) * dimer_ind
    return Data(
        ZA=atomic_props_A.x,
        RA=atomic_props_A.R,
        ZB=atomic_props_B.x,
        RB=atomic_props_B.R,
        # short range, intermolecular edges
        e_ABsr_source=e_ABsr_source,
        e_ABsr_target=e_ABsr_target,
        dimer_ind=dimer_ind,
        # long range, intermolecular edges
        e_ABlr_source=e_ABlr_source,
        e_ABlr_target=e_ABlr_target,
        dimer_ind_lr=dimer_ind,
        # intramonomer edges (monomer A)
        e_AA_source=e_AA_source,
        e_AA_target=e_AA_target,
        molecule_ind_A=atomic_props_A.molecule_ind,
        # intramonomer edges (monomer B)
        e_BB_source=e_BB_source,
        e_BB_target=e_BB_target,
        molecule_ind_B=atomic_props_B.molecule_ind,
        # monomer charges
        total_charge_A=atomic_props_A.total_charge,
        total_charge_B=atomic_props_B.total_charge,
        **kwargs,  # allows for additional properties to be passed in
    )


def natural_key(text):
    return [int(s) if s.isdigit() else s for s in re.split(r"(\d+)", text)]


###############################
#######   PairDataset   #######
###############################


def pairwise_edges(R, r_cut, full_indices=False):
    natom = R.size(0)

    RA = R.unsqueeze(0).repeat(natom, 1, 1)  # [natom x natom x 3]
    RB = R.unsqueeze(1).repeat(1, natom, 1)  # [natom x natom x 3]

    dist = torch.norm(RA - RB, dim=2)

    mask = (dist < r_cut) & (dist > 0.0)
    edges = torch.where(mask)  # indices where the mask is true
    if full_indices:
        full_edges = torch.where((dist > 0.0))
        return (
            edges[0].long(),
            edges[1].long(),
            full_edges[0].long(),
            full_edges[1].long(),
        )
    return edges[0].long(), edges[1].long()


def pairwise_edges_im(RA, RB, r_cut_im, full_indices=False):
    natomA = RA.shape[0]
    natomB = RB.shape[0]

    RA_temp = RA.unsqueeze(1).repeat(1, natomB, 1)  # [natomA x natomB x 3]
    RB_temp = RB.unsqueeze(0).repeat(natomA, 1, 1)  # [natomA x natomB x 3]

    dist = torch.norm(RA_temp - RB_temp, dim=2)

    mask = dist <= r_cut_im
    # dimensions [n_edge x 2]
    edges_sr = torch.nonzero(mask, as_tuple=False).long()
    # dimensions [n_edge x 2]
    edges_lr = torch.nonzero(~mask, as_tuple=False).long()

    if full_indices:
        full_edges = torch.cat([edges_sr, edges_lr], dim=0)
        return (
            edges_sr[:, 0],
            edges_sr[:, 1],
            edges_lr[:, 0],
            edges_lr[:, 1],
            full_edges[0].long(),
            full_edges[1].long(),
        )
    return edges_sr[:, 0], edges_sr[:, 1], edges_lr[:, 0], edges_lr[:, 1]


def ap2_fused_collate_update(batch):
    """
    Need to update the edge_index values so that each molecule has a unique
    set of indices. Then, the data.molecule_ind can be used to group
    atoms into molecules during a forward pass.
    """
    monA_edge_offset, monB_edge_offset = 0, 0
    local_e_ABsr_source = []
    local_e_ABsr_target = []
    local_e_ABlr_source = []
    local_e_ABlr_target = []

    local_e_AA_source = []
    local_e_AA_target = []
    local_e_BB_source = []
    local_e_BB_target = []

    for i, data in enumerate(batch):
        # need dimer ind to be index size of short-range edges
        data.dimer_ind = (
            torch.ones(data.e_ABsr_source.size(0), dtype=data.dimer_ind.dtype) * i
        )
        data.dimer_ind_lr = (
            torch.ones(data.e_ABlr_source.size(0), dtype=data.dimer_ind_lr.dtype) * i
        )
        data.molecule_ind_A = (
            torch.ones(data.molecule_ind_A.size(0), dtype=data.molecule_ind_A.dtype) * i
        )
        data.molecule_ind_B = (
            torch.ones(data.molecule_ind_B.size(0), dtype=data.molecule_ind_B.dtype) * i
        )
        local_e_ABsr_source.append(data.e_ABsr_source.clone() + monA_edge_offset)
        local_e_ABsr_target.append(data.e_ABsr_target.clone() + monB_edge_offset)
        local_e_ABlr_source.append(data.e_ABlr_source.clone() + monA_edge_offset)
        local_e_ABlr_target.append(data.e_ABlr_target.clone() + monB_edge_offset)

        # Monomer edges
        local_e_AA_source.append(data.e_AA_source.clone() + monA_edge_offset)
        local_e_AA_target.append(data.e_AA_target.clone() + monA_edge_offset)
        local_e_BB_source.append(data.e_BB_source.clone() + monB_edge_offset)
        local_e_BB_target.append(data.e_BB_target.clone() + monB_edge_offset)

        monA_edge_offset += data.RA.size(0)
        monB_edge_offset += data.RB.size(0)
    molecule_ind_A = torch.cat([data.molecule_ind_A for data in batch], dim=0)
    molecule_ind_B = torch.cat([data.molecule_ind_B for data in batch], dim=0)
    natom_per_mol_A = torch.bincount(molecule_ind_A)
    natom_per_mol_B = torch.bincount(molecule_ind_B)
    y = torch.stack([data.y for data in batch], dim=0)
    batched_data = Data(
        y=y,
        ZA=torch.cat([data.ZA for data in batch], dim=0),
        RA=torch.cat([data.RA for data in batch], dim=0),
        ZB=torch.cat([data.ZB for data in batch], dim=0),
        RB=torch.cat([data.RB for data in batch], dim=0),
        e_AA_source=torch.cat(local_e_AA_source, dim=0),
        e_AA_target=torch.cat(local_e_AA_target, dim=0),
        e_BB_source=torch.cat(local_e_BB_source, dim=0),
        e_BB_target=torch.cat(local_e_BB_target, dim=0),
        molecule_ind_A=molecule_ind_A,
        molecule_ind_B=molecule_ind_B,
        natom_per_mol_A=natom_per_mol_A,
        natom_per_mol_B=natom_per_mol_B,
        e_ABsr_source=torch.cat(local_e_ABsr_source, dim=0),
        e_ABsr_target=torch.cat(local_e_ABsr_target, dim=0),
        e_ABlr_source=torch.cat(local_e_ABlr_source, dim=0),
        e_ABlr_target=torch.cat(local_e_ABlr_target, dim=0),
        dimer_ind=torch.cat([data.dimer_ind for data in batch], dim=0),
        dimer_ind_lr=torch.cat([data.dimer_ind_lr for data in batch], dim=0),
        total_charge_A=torch.tensor(
            [data.total_charge_A for data in batch], dtype=batch[0].total_charge_A.dtype
        ),
        total_charge_B=torch.tensor(
            [data.total_charge_B for data in batch], dtype=batch[0].total_charge_B.dtype
        ),
    )
    return batched_data


def ap2_fused_collate_update_no_target(batch):
    """
    Need to update the edge_index values so that each molecule has a unique
    set of indices. Then, the data.molecule_ind can be used to group
    atoms into molecules during a forward pass.
    """
    monA_edge_offset, monB_edge_offset = 0, 0
    local_e_ABsr_source = []
    local_e_ABsr_target = []
    local_e_ABlr_source = []
    local_e_ABlr_target = []
    local_e_AA_source = []
    local_e_AA_target = []
    local_e_BB_source = []
    local_e_BB_target = []
    local_indA = []
    local_indB = []
    for i, data in enumerate(batch):
        data.dimer_ind = (
            torch.ones(data.e_ABsr_source.size(0), dtype=data.dimer_ind.dtype) * i
        )
        data.dimer_ind_lr = (
            torch.ones(data.e_ABlr_source.size(0), dtype=data.dimer_ind_lr.dtype) * i
        )
        data.molecule_ind_A = (
            torch.ones(data.molecule_ind_A.size(0), dtype=data.molecule_ind_A.dtype) * i
        )
        data.molecule_ind_B = (
            torch.ones(data.molecule_ind_B.size(0), dtype=data.molecule_ind_B.dtype) * i
        )
        local_e_ABsr_source.append(data.e_ABsr_source.clone() + monA_edge_offset)
        local_e_ABsr_target.append(data.e_ABsr_target.clone() + monB_edge_offset)
        local_e_ABlr_source.append(data.e_ABlr_source.clone() + monA_edge_offset)
        local_e_ABlr_target.append(data.e_ABlr_target.clone() + monB_edge_offset)
        local_e_AA_source.append(data.e_AA_source.clone() + monA_edge_offset)
        local_e_AA_target.append(data.e_AA_target.clone() + monA_edge_offset)
        local_e_BB_source.append(data.e_BB_source.clone() + monB_edge_offset)
        local_e_BB_target.append(data.e_BB_target.clone() + monB_edge_offset)

        monA_edge_offset += data.RA.size(0)
        monB_edge_offset += data.RB.size(0)

        local_indA.append(torch.ones(data.RA.size(0), dtype=data.dimer_ind.dtype) * i)
        local_indB.append(
            torch.ones(data.RB.size(0), dtype=data.dimer_ind_lr.dtype) * i
        )
    molecule_ind_A = torch.cat([data.molecule_ind_A for data in batch], dim=0)
    molecule_ind_B = torch.cat([data.molecule_ind_B for data in batch], dim=0)
    natom_per_mol_A = torch.bincount(molecule_ind_A)
    natom_per_mol_B = torch.bincount(molecule_ind_B)
    batched_data = Data(
        ZA=torch.cat([data.ZA for data in batch], dim=0),
        RA=torch.cat([data.RA for data in batch], dim=0),
        ZB=torch.cat([data.ZB for data in batch], dim=0),
        RB=torch.cat([data.RB for data in batch], dim=0),
        e_AA_source=torch.cat(local_e_AA_source, dim=0),
        e_AA_target=torch.cat(local_e_AA_target, dim=0),
        e_BB_source=torch.cat(local_e_BB_source, dim=0),
        e_BB_target=torch.cat(local_e_BB_target, dim=0),
        molecule_ind_A=molecule_ind_A,
        molecule_ind_B=molecule_ind_B,
        natom_per_mol_A=natom_per_mol_A,
        natom_per_mol_B=natom_per_mol_B,
        e_ABsr_source=torch.cat(local_e_ABsr_source, dim=0),
        e_ABsr_target=torch.cat(local_e_ABsr_target, dim=0),
        e_ABlr_source=torch.cat(local_e_ABlr_source, dim=0),
        e_ABlr_target=torch.cat(local_e_ABlr_target, dim=0),
        dimer_ind=torch.cat([data.dimer_ind for data in batch], dim=0),
        dimer_ind_lr=torch.cat([data.dimer_ind_lr for data in batch], dim=0),
        total_charge_A=torch.tensor(
            [data.total_charge_A for data in batch], dtype=batch[0].total_charge_A.dtype
        ),
        total_charge_B=torch.tensor(
            [data.total_charge_B for data in batch], dtype=batch[0].total_charge_B.dtype
        ),
        indA=torch.cat(local_indA, dim=0),
        indB=torch.cat(local_indB, dim=0),
    )
    return batched_data


def ap2_fused_collate_update_no_target_monomer_indices(batch):
    """
    Need to update the edge_index values so that each molecule has a unique
    set of indices. Then, the data.molecule_ind can be used to group
    atoms into molecules during a forward pass.
    """
    monA_edge_offset, monB_edge_offset = 0, 0
    local_e_ABsr_source = []
    local_e_ABsr_target = []
    local_e_ABlr_source = []
    local_e_ABlr_target = []
    local_e_AA_source = []
    local_e_AA_target = []
    local_e_BB_source = []
    local_e_BB_target = []
    local_indA = []
    local_indB = []
    for i, data in enumerate(batch):
        data.dimer_ind = (
            torch.ones(data.e_ABsr_source.size(0), dtype=data.dimer_ind.dtype) * i
        )
        data.dimer_ind_lr = (
            torch.ones(data.e_ABlr_source.size(0), dtype=data.dimer_ind_lr.dtype) * i
        )
        local_e_ABsr_source.append(data.e_ABsr_source.clone() + monA_edge_offset)
        local_e_ABsr_target.append(data.e_ABsr_target.clone() + monB_edge_offset)
        local_e_ABlr_source.append(data.e_ABlr_source.clone() + monA_edge_offset)
        local_e_ABlr_target.append(data.e_ABlr_target.clone() + monB_edge_offset)
        local_e_AA_source.append(data.e_AA_source.clone() + monA_edge_offset)
        local_e_AA_target.append(data.e_AA_target.clone() + monA_edge_offset)
        local_e_BB_source.append(data.e_BB_source.clone() + monB_edge_offset)
        local_e_BB_target.append(data.e_BB_target.clone() + monB_edge_offset)

        monA_edge_offset += data.RA.size(0)
        monB_edge_offset += data.RB.size(0)
        local_indA.append(torch.ones(data.RA.size(0), dtype=data.dimer_ind.dtype) * i)
        local_indB.append(
            torch.ones(data.RB.size(0), dtype=data.dimer_ind_lr.dtype) * i
        )
    batched_data = Data(
        ZA=torch.cat([data.ZA for data in batch], dim=0),
        RA=torch.cat([data.RA for data in batch], dim=0),
        ZB=torch.cat([data.ZB for data in batch], dim=0),
        RB=torch.cat([data.RB for data in batch], dim=0),
        e_AA_source=torch.cat(local_e_AA_source, dim=0),
        e_AA_target=torch.cat(local_e_AA_target, dim=0),
        e_BB_source=torch.cat(local_e_BB_source, dim=0),
        e_BB_target=torch.cat(local_e_BB_target, dim=0),
        e_ABsr_source=torch.cat(local_e_ABsr_source, dim=0),
        e_ABsr_target=torch.cat(local_e_ABsr_target, dim=0),
        e_ABlr_source=torch.cat(local_e_ABlr_source, dim=0),
        e_ABlr_target=torch.cat(local_e_ABlr_target, dim=0),
        dimer_ind=torch.cat([data.dimer_ind for data in batch], dim=0),
        dimer_ind_lr=torch.cat([data.dimer_ind_lr for data in batch], dim=0),
        total_charge_A=torch.tensor(
            [data.total_charge_A for data in batch], dtype=batch[0].total_charge_A.dtype
        ),
        total_charge_B=torch.tensor(
            [data.total_charge_B for data in batch], dtype=batch[0].total_charge_B.dtype
        ),
        qA=torch.cat([data.qA for data in batch], dim=0),
        muA=torch.cat([data.muA for data in batch], dim=0),
        quadA=torch.cat([data.quadA for data in batch], dim=0),
        hlistA=torch.cat([data.hlistA for data in batch], dim=0),
        qB=torch.cat([data.qB for data in batch], dim=0),
        muB=torch.cat([data.muB for data in batch], dim=0),
        quadB=torch.cat([data.quadB for data in batch], dim=0),
        hlistB=torch.cat([data.hlistB for data in batch], dim=0),
        indA=torch.cat(local_indA, dim=0),
        indB=torch.cat(local_indB, dim=0),
    )
    return batched_data


class APNet2_fused_DataLoader(torch.utils.data.DataLoader):
    r"""A data loader which merges data objects from a
    :class:`torch_geometric.data.Dataset` to a mini-batch.
    Data objects can be either of type :class:`~torch_geometric.data.Data` or
    :class:`~torch_geometric.data.HeteroData`.

    Args:
        dataset (Dataset): The dataset from which to load the data.
        batch_size (int, optional): How many samples per batch to load.
            (default: :obj:`1`)
        shuffle (bool, optional): If set to :obj:`True`, the data will be
            reshuffled at every epoch. (default: :obj:`False`)
        follow_batch (List[str], optional): Creates assignment batch
            vectors for each key in the list. (default: :obj:`None`)
        exclude_keys (List[str], optional): Will exclude each key in the
            list. (default: :obj:`None`)
        **kwargs (optional): Additional arguments of
            :class:`torch.utils.data.DataLoader`.
    """

    def __init__(
        self,
        dataset: Union[Dataset, Sequence[BaseData], DatasetAdapter],
        batch_size: int = 1,
        shuffle: bool = False,
        follow_batch: Optional[List[str]] = None,
        exclude_keys: Optional[List[str]] = None,
        collate_fn=None,  # atomic_collate_update,
        **kwargs,
    ):
        if collate_fn is None:
            # Save for PyTorch Lightning < 1.6:
            self.follow_batch = follow_batch
            self.exclude_keys = exclude_keys

            self.collator = atomic_datasets.Collater(
                dataset, follow_batch, exclude_keys
            )
            self.collate_fn = self.collator.collate_fn
        else:
            self.collate_fn = collate_fn

        if isinstance(dataset, OnDiskDataset):
            dataset = range(len(dataset))

        super().__init__(
            dataset,
            batch_size,
            shuffle,
            collate_fn=self.collate_fn,
            **kwargs,
        )


def ap2_fused_setup(molA_data, molB_data, atom_model, r_cut, r_cut_im, index=0):
    batch_A = atomic_datasets.atomic_collate_update_no_target(molA_data)
    qAs, muAs, thAs, hlistAs = atom_model.predict_multipoles_batch(batch_A)
    batch_B = atomic_datasets.atomic_collate_update_no_target(molB_data)
    qBs, muBs, thBs, hlistBs = atom_model.predict_multipoles_batch(batch_B)
    dimer_data = []
    for j in range(len(molA_data)):
        atomic_props_A = molA_data[j]
        atomic_props_B = molB_data[j]
        qA, muA, quadA, hlistA = qAs[j], muAs[j], thAs[j], hlistAs[j]
        qB, muB, quadB, hlistB = qBs[j], muBs[j], thBs[j], hlistBs[j]
        if len(qA.size()) == 0:
            qA = qA.unsqueeze(0).unsqueeze(0)
        elif len(qA.size()) == 1:
            qA = qA.unsqueeze(-1)
        if len(qB.size()) == 0:
            qB = qB.unsqueeze(0).unsqueeze(0)
        elif len(qB.size()) == 1:
            qB = qB.unsqueeze(-1)
        e_AA_source, e_AA_target = pairwise_edges(atomic_props_A.R, r_cut)
        e_BB_source, e_BB_target = pairwise_edges(atomic_props_B.R, r_cut)
        e_ABsr_source, e_ABsr_target, e_ABlr_source, e_ABlr_target = pairwise_edges_im(
            atomic_props_A.R, atomic_props_B.R, r_cut_im
        )
        dimer_ind = torch.ones((1), dtype=torch.long) * index
        data = Data(
            ZA=atomic_props_A.x.long(),
            RA=atomic_props_A.R,
            ZB=atomic_props_B.x.long(),
            RB=atomic_props_B.R,
            # short range, intermolecular edges
            e_ABsr_source=e_ABsr_source.long(),
            e_ABsr_target=e_ABsr_target.long(),
            dimer_ind=dimer_ind.long(),
            # long range, intermolecular edges
            e_ABlr_source=e_ABlr_source.long(),
            e_ABlr_target=e_ABlr_target.long(),
            dimer_ind_lr=dimer_ind.long(),
            # intramonomer edges (monomer A)
            e_AA_source=e_AA_source.long(),
            e_AA_target=e_AA_target.long(),
            # intramonomer edges (monomer B)
            e_BB_source=e_BB_source.long(),
            e_BB_target=e_BB_target.long(),
            # monomer charges
            total_charge_A=atomic_props_A.total_charge,
            total_charge_B=atomic_props_B.total_charge,
            # monomer A properties
            qA=qA,
            muA=muA,
            quadA=quadA,
            hlistA=hlistA,
            # monomer B properties
            qB=qB,
            muB=muB,
            quadB=quadB,
            hlistB=hlistB,
        )
        data = data.cpu()
        dimer_data.append(data)
    return dimer_data


class ap2_fused_module_dataset(Dataset):
    def __init__(
        self,
        root,
        transform=None,
        pre_transform=None,
        r_cut=5.0,
        r_cut_im=8.0,
        spec_type=1,
        max_size=None,
        force_reprocess=False,
        skip_processed=True,
        skip_compile=False,
        # only need for processing
        atom_model_path=resources.files("apnet_pt").joinpath(
            "models", "am_ensemble", "am_0.pt"
        ),
        atom_model=None,
        batch_size=16,
        atomic_batch_size=200,
        # DO NOT CHANGE UNLESS YOU WANT TO RE-PROCESS THE DATASET
        datapoint_storage_n_objects=1000,
        in_memory=False,
        num_devices=1,
        split="all",  # train, test
        print_level=1,
        qcel_molecules: Optional[List[qcel.models.Molecule]] = None,
        energy_labels: Optional[List[float]] = None,
        random_seed=42,
        check_monomer_validity=True,
    ):
        """
        spec_type definitions:
            1. regular
            2. AP2 paper train/test split
            5. testing small
            6. testing 12k
            7. testing 12k but creating batch of 16 to avoid any collating and reduce large I/O issues (potentially)
            None: assumes that data is passed as qcel_molecules and energy labels
        """
        self.print_level = print_level
        try:
            assert spec_type in [1, 2, 5, 6, 7, 8, 9, None]
        except Exception:
            print("Currently spec_type must be 1 or 2 for SAPT0/jun-cc-pVDZ")
            raise ValueError
        self.spec_type = spec_type

        self.qcel_molecules = None
        self.energy_labels = None
        # Store qcel_molecules and energy_labels if provided
        if qcel_molecules is not None and energy_labels is not None:
            self.qcel_molecules = qcel_molecules
            self.energy_labels = energy_labels
            if len(qcel_molecules) != len(energy_labels):
                raise ValueError(
                    "Length of qcel_molecules and energy_labels must match"
                )
            print(
                f"Received {len(qcel_molecules)}"
                " QCElemental molecules with energy labels"
            )

        self.MAX_SIZE = max_size
        self.random_seed = random_seed
        self.in_memory = in_memory
        self.split = split
        self.r_cut = r_cut
        self.r_cut_im = r_cut_im
        self.force_reprocess = force_reprocess
        self.atomic_batch_size = atomic_batch_size
        self.check_monomer_validity = check_monomer_validity
        self.batch_size = batch_size
        self.training_batch_size = batch_size
        self.datapoint_storage_n_objects = datapoint_storage_n_objects
        self.points_per_file = self.datapoint_storage_n_objects
        self.skip_compile = skip_compile
        if self.in_memory:
            self.points_per_file = 1
        self.data = []
        self.skip_processed = skip_processed
        if os.path.exists(root) is False:
            os.makedirs(root, exist_ok=True)
        if atom_model is not None:
            if isinstance(atom_model, AtomModel):
                self.atom_model = atom_model
            else:
                self.atom_model = AtomModel(
                    ds_root=None,
                    ignore_database_null=True,
                )
                self.atom_model.model = atom_model
            if not skip_compile:
                self.atom_model.model = torch.compile(
                    self.atom_model.model, dynamic=True
                )
        elif atom_model_path is not None and not self.skip_processed:
            self.atom_model = AtomModel(
                pre_trained_model_path=atom_model_path,
                ds_root=None,
                ignore_database_null=True,
            )
            self.atom_model.model.to(self.atom_model.device)
            torch._dynamo.config.dynamic_shapes = True
            torch._dynamo.config.capture_dynamic_output_shape_ops = True
            torch._dynamo.config.capture_scalar_outputs = True
            if not skip_compile:
                self.atom_model.model = torch.compile(
                    self.atom_model.model, dynamic=True
                )
        print(f"{root=}, {self.spec_type=}, {self.in_memory=}")
        super(ap2_fused_module_dataset, self).__init__(root, transform, pre_transform)
        if self.force_reprocess:
            self.force_reprocess = False
            super(ap2_fused_module_dataset, self).__init__(
                root, transform, pre_transform
            )
        if self.in_memory:
            self.get = self.get_in_memory
        self.batch_size = batch_size
        self.active_idx_data = None
        self.active_data = None

    @property
    def raw_file_names(self):
        # TODO: enable users to specify data source via QCArchive, url, or local file
        # spec_1 = "spec_1" # 'SAPT0/jun-cc-pVDZ'
        if self.spec_type == 2:
            return [
                "1600K_train_dimers-fixed.pkl",
                "1600K_test_dimers-fixed.pkl",
            ]
        elif self.spec_type == 5:
            return [
                "t_train.pkl",
                "t_test.pkl",
            ]
        elif self.spec_type == 6:
            return [
                "t_train10k.pkl",
                "t_test2k.pkl",
            ]
        elif self.spec_type == 7:
            return [
                "t_train_100.pkl",
                "t_test_20.pkl",
            ]
        elif self.spec_type == 8:
            return [
                "t_val_19.pkl",
            ]
        elif self.spec_type == 9:
            return [
                "t_train_19.pkl",
                "t_test_19.pkl",
            ]
        elif self.spec_type is None:
            os.system(f"touch {self.raw_dir}/tmp.txt")
            return ["tmp.txt"]
        else:
            return [
                "splinter_spec1.pkl",
            ]

    def reprocess_file_names(self):
        if self.force_reprocess:
            return ["file"]
        else:
            if self.split == "train":
                file_cmd = f"{self.root}/processed/dimer_ap2_fused_train_spec_{
                    self.spec_type
                }_*.pt"
            elif self.split == "test":
                file_cmd = f"{self.root}/processed/dimer_ap2_fused_test_spec_{
                    self.spec_type
                }_*.pt"
            else:
                file_cmd = (
                    f"{self.root}/processed/dimer_ap2_fused_spec_{self.spec_type}_*.pt"
                )
            spec_files = glob(file_cmd)
            spec_files = [i.split("/")[-1] for i in spec_files]
            if len(spec_files) > 0:
                # want to preserve idx ordering
                spec_files.sort(key=natural_key)
                if self.MAX_SIZE is not None:
                    max_size = int(self.MAX_SIZE / self.datapoint_storage_n_objects)
                    # if max_size == 0:
                    #     raise ValueError(
                    #         "MAX_SIZE must be greater than datapoint_storage_n_objects"
                    #     )
                if self.MAX_SIZE is not None:
                    if len(spec_files) > max_size and max_size > 0:
                        spec_files = spec_files[:max_size]
                    elif len(spec_files) > max_size:
                        spec_files = spec_files[:1]
                return spec_files
            else:
                # Forces a re-processing of the dataset
                return ["dimer_missing.pt"]

    @property
    def processed_file_names(self):
        return self.reprocess_file_names()

    def download(self):
        if self.energy_labels and self.qcel_molecules:
            return

        print(
            "Downloading Splinter dataset of ~1.6M Dimers. This might take a while..."
        )
        splinter_spec_1_files = [
            "https://figshare.com/ndownloader/files/39449167",
            "https://figshare.com/ndownloader/files/40271983",
            "https://figshare.com/ndownloader/files/40271989",
            "https://figshare.com/ndownloader/files/40272001",
            "https://figshare.com/ndownloader/files/40552931",
            "https://figshare.com/ndownloader/files/40272022",
            "https://figshare.com/ndownloader/files/40272040",
            "https://figshare.com/ndownloader/files/40272052",
            "https://figshare.com/ndownloader/files/40272061",
            "https://figshare.com/ndownloader/files/40272064",
        ]
        for n, i in enumerate(splinter_spec_1_files):
            download_url(
                i,
                self.raw_dir,
                filename=f"splinter_spec1_{n}.tar.gz",
            )
        if not os.path.exists(f"{self.raw_dir}/dimerpairs"):
            for i in range(len(splinter_spec_1_files)):
                with tarfile.open(f"{self.raw_dir}/splinter_spec1_{i}.tar.gz") as tar:
                    tar.extractall(self.raw_dir)
        return

    def process(self):
        self.data = []
        idx = 0
        data_objects = []
        # Handle direct qcel_mols input
        RAs, RBs, ZAs, ZBs, TQAs, TQBs, targets = [], [], [], [], [], [], []
        if self.qcel_molecules is not None and self.energy_labels is not None:
            print("Processing directly from provided QCElemental molecules...")
            split_name = f"_{self.split}" if self.split != "all" else ""

            # Process directly from qcel_mols and energy_labels
            for mol in self.qcel_molecules:
                # Extract monomer data from dimer
                monA, monB = mol.get_fragment(0), mol.get_fragment(1)

                # Get coordinates and atomic numbers for each monomer
                RA = torch.tensor(monA.geometry, dtype=torch.float32) * constants.au2ang
                RB = torch.tensor(monB.geometry, dtype=torch.float32) * constants.au2ang
                ZA = torch.tensor(monA.atomic_numbers, dtype=torch.int64)
                ZB = torch.tensor(monB.atomic_numbers, dtype=torch.int64)

                # Calculate total charges
                TQA = torch.tensor(monA.molecular_charge, dtype=torch.float32)
                TQB = torch.tensor(monB.molecular_charge, dtype=torch.float32)

                RAs.append(RA)
                RBs.append(RB)
                ZAs.append(ZA)
                ZBs.append(ZB)
                TQAs.append(TQA)
                TQBs.append(TQB)
            targets = self.energy_labels

            if self.MAX_SIZE is not None and len(RAs) > self.MAX_SIZE:
                RAs = RAs[: self.MAX_SIZE]
                RBs = RBs[: self.MAX_SIZE]
                ZAs = ZAs[: self.MAX_SIZE]
                ZBs = ZBs[: self.MAX_SIZE]
                TQAs = TQAs[: self.MAX_SIZE]
                TQBs = TQBs[: self.MAX_SIZE]
                targets = targets[: self.MAX_SIZE]

            print(
                f"Processing {len(RAs)} dimers from provided QCElemental molecules..."
            )
        else:
            for raw_path in self.raw_paths:
                split_name = ""
                if self.spec_type in [2, 5, 6, 7, 9]:
                    split_name = f"_{self.split}" if self.split != "all" else ""
                    print(f"{split_name=}")
                    if self.split not in Path(raw_path).stem:
                        print(f"{self.split} is skipping {raw_path}")
                        continue
                print(f"raw_path: {raw_path}")
                print("Loading dimers...")
                RA, RB, ZA, ZB, TQA, TQB, target = util.load_dimer_dataset(
                    raw_path,
                    self.MAX_SIZE,
                    return_qcel_mols=False,
                    return_qcel_mons=False,
                    columns=["Elst_aug", "Exch_aug", "Ind_aug", "Disp_aug"],
                    random_seed_shuffle=self.random_seed,
                )
                RAs.extend(RA)
                RBs.extend(RB)
                ZAs.extend(ZA)
                ZBs.extend(ZB)
                TQAs.extend(TQA)
                TQBs.extend(TQB)
                targets.extend(target)
        print("Creating data objects...")
        t1 = time()
        t2 = time()
        print(f"{len(RAs)=}, {self.atomic_batch_size=}, {self.batch_size=}")
        for i in range(len(RAs)):
            if self.skip_processed:
                datapath = osp.join(
                    self.processed_dir,
                    f"dimer_ap2_fused{split_name}_spec_{self.spec_type}_{
                        idx // self.points_per_file
                    }.pt",
                )
                if osp.exists(datapath):
                    idx += 1
                    continue
            y = torch.tensor(targets[i], dtype=torch.float32)
            data = dimer_fused_data(
                RAs[i],
                ZAs[i],
                TQAs[i],
                RBs[i],
                ZBs[i],
                TQBs[i],
                dimer_ind=i,
                r_cut=self.r_cut,
                r_cut_im=self.r_cut_im,
                check_validity=self.check_monomer_validity,
                y=y,
            )
            if data is None:
                print(data)
                print(f"Skipping invalid dimer index {i}")
                continue
            data = data.cpu()
            if self.pre_filter is not None and not self.pre_filter(data):
                continue
            data_objects.append(data)
            # Normally would store the data object to individual files,
            # but at 1.67M dimers, this is too many files. Need to
            # store self.datapoint_storage_n_objects (like 1000) dimers per file
            if len(data_objects) == self.points_per_file:
                if self.in_memory:
                    data_objects = data_objects[0]
                if self.in_memory:
                    self.data.append(data_objects)
                else:
                    datapath = osp.join(
                        self.processed_dir,
                        f"dimer_ap2_fused{split_name}_spec_{self.spec_type}_{
                            idx // self.points_per_file
                        }.pt",
                    )
                    if self.print_level >= 2:
                        print(f"Saving to {datapath}")
                        print(len(data_objects))
                    torch.save(data_objects, datapath)
                data_objects = []
                if self.MAX_SIZE is not None and idx > self.MAX_SIZE:
                    break
            idx += 1
        if self.print_level >= 2:
            print(f"{i}/{len(RAs)}, {time() - t2:.2f}s, {time() - t1:.2f}s")
        elif self.print_level >= 1 and idx % 1000:
            print(f"{i}/{len(RAs)}, {time() - t2:.2f}s, {time() - t1:.2f}s")
        t2 = time()
        if len(data_objects) > 0:
            if self.in_memory:
                data_objects = data_objects[0]
            if self.in_memory:
                self.data.append(data_objects)
            else:
                datapath = osp.join(
                    self.processed_dir,
                    f"dimer_ap2_fused{split_name}_spec_{self.spec_type}_{
                        idx // self.points_per_file
                    }.pt",
                )
                if self.print_level >= 2:
                    print(f"Final Saving to {datapath}")
                    print(len(data_objects))
                torch.save(data_objects, datapath)
        return

    def len(self):
        if self.in_memory:
            return len(self.data)

        d = torch.load(
            osp.join(self.processed_dir, self.processed_file_names[-1]),
            weights_only=False,
        )
        return (
            len(self.processed_file_names) - 1
        ) * self.datapoint_storage_n_objects + len(d)

    def get(self, idx):
        idx_datapath = idx // self.datapoint_storage_n_objects
        obj_ind = idx % self.datapoint_storage_n_objects
        if self.active_idx_data == idx_datapath:
            return self.active_data[obj_ind]
        split_name = ""
        if self.spec_type in [2, 5, 6, 7, 9, None]:
            split_name = f"_{self.split}" if self.split != "all" else ""
        datapath = osp.join(
            self.processed_dir,
            f"dimer_ap2_fused{split_name}_spec_{self.spec_type}_{idx_datapath}.pt",
        )
        self.active_data = torch.load(datapath, weights_only=False)
        try:
            self.active_data[obj_ind]
        except Exception:
            print(
                f"Error loading {datapath}\n    at {
                    idx = }, {idx_datapath = }, {obj_ind = }"
            )
        return self.active_data[obj_ind]

    def get_in_memory(self, idx):
        """Method for retrieving data when in_memory=True"""
        return self.data[idx]
