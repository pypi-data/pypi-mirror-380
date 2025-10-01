import shutil
import warnings
from pathlib import Path
from typing import Any, Optional, Callable

import MDAnalysis as mda
import parmed
from rdkit import Chem
from rdkit.Chem import rdFMCS

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # ignore `BiopythonDeprecationWarning` warning
    from MDAnalysis import analysis


from amberflow.artifacts import (
    BasePeriodicBox,
    BaseComplexPeriodicBox,
    LigandLib,
    LigandFrcmod,
    ArtifactContainer,
    AmberSC1Mask,
    AmberSC2Mask,
    BaseAmberMaskString,
    AmberTI1Mask,
    AmberTI2Mask,
    CC1Atomlist,
    SC1Atomlist,
    CC2Atomlist,
    SC2Atomlist,
    BaseAtomList,
    ArtifactRegistry,
)
from amberflow.artifacts.structure import BinderLigandPDB, get_biomolecule2
from amberflow.customartifacts import (
    BaseDockTargetStructureFile,
    DockBinderLib,
    DockBinderFrcmod,
    BaseDockBinderStructureFile,
    BaseDockComplexStructureFile,
    DockProteinLigandComplexPDB,
)
from amberflow.primitives import (
    filepath_t,
    dirpath_t,
    WorkNodeRunningError,
    patch_pdb_lib,
    concatenate_pdbs,
    assign_chain_ids,
)
from amberflow.worknodes import (
    worknodehelper,
    get_periodic_box_parameters_pdb,
    BaseSingleWorkNode,
    runiverse,
    wuniverse,
)

__all__ = ("BuildDockTemplate",)

AlignmentCallable = Callable[[dict[str, filepath_t], dict[str, filepath_t], dict[str, Any]], None]
SelectionCallable = Callable[[filepath_t, filepath_t], dict[str, Any]]


@worknodehelper(
    file_exists=True,
    input_artifact_types=(
        BinderLigandPDB,
        LigandLib,
        LigandFrcmod,
        BaseDockTargetStructureFile,
        BaseDockBinderStructureFile,
        DockBinderLib,
        DockBinderFrcmod,
    ),
    optional_artifact_types=(BasePeriodicBox,),
    need_all_input_artifacts=False,
    output_artifact_types=(
        BaseDockComplexStructureFile,
        LigandLib,
        LigandFrcmod,
        DockBinderLib,
        DockBinderFrcmod,
        BasePeriodicBox,
        BaseAmberMaskString,
        BaseAtomList,
    ),
)
class BuildDockTemplate(BaseSingleWorkNode):
    """ """

    RESNAME_LIG: dict[str, str] = {"reference": "L00", "target": "L01"}
    MASK_LIG: dict[str, str] = {"reference": ":1", "target": ":2"}

    SELECTION_HANDLERS: dict[str, str] = {
        "amideplus": "amideplus",
        "amide": "amide",
        "mcs": "mcs",
    }
    selector: SelectionCallable

    ALIGNMENT_HANDLERS: dict[str, str] = {
        "rmsd": "rmsd",
        "commoncore": "commoncore",
        "rmsdcommoncore": "rmsdcommoncore",
    }
    aligner: AlignmentCallable
    MAX_CUTOFF: float = 10.0

    CONFIGURABLE: dict[str, dict[str, str]] = {"selector": SELECTION_HANDLERS, "aligner": ALIGNMENT_HANDLERS}

    def __init__(
        self,
        wnid: str,
        *args,
        selector: str = "amideplus",
        aligner: str = "rmsd",
        rebuild_sc: bool = True,
        cc_contacts_cutoff: float = 3,
        min_cc_contacts: int = 4,
        cc_contacts_step_size: float = 0.1,
        sc_contacts_nofreeze_cutoff: float = 3,
        **kwargs,
    ) -> None:
        super().__init__(
            wnid=wnid,
            *args,
            **kwargs,
        )
        for param_str, handlers in self.CONFIGURABLE.items():
            param_val = locals()[param_str]
            try:
                handler = getattr(self, handlers[param_val])
                setattr(self, param_str, handler)
            except KeyError:
                err_msg = f"{param_val} method {param_val} not recognized. Available methods: {list(handlers.keys())}"
                raise ValueError(err_msg)
        self.rebuild_sc = rebuild_sc
        self.cc_contacts_cutoff = cc_contacts_cutoff
        self.min_cc_contacts = min_cc_contacts
        self.cc_contacts_step_size = cc_contacts_step_size
        self.sc_contacts_nofreeze_cutoff = sc_contacts_nofreeze_cutoff

    def _run(
        self,
        *,
        cwd: dirpath_t,
        sysname: str,
        binpath: Optional[filepath_t] = None,
        **kwargs,
    ) -> ArtifactContainer:
        try:
            box = self.input_artifacts["BasePeriodicBox"]
        except KeyError:
            biomol = get_biomolecule2(self.input_artifacts, self.node_logger)
            boxtype = ArtifactRegistry.concrete_artifact(BaseComplexPeriodicBox, {biomol, "ligand"})
            box = boxtype(get_periodic_box_parameters_pdb(Path(self.input_artifacts["BaseDockTargetStructureFile"])))
        self.node_logger.info(f"Got box:\n{box}")

        # frcmod files are not modified
        in_ref_frcmod = Path(self.input_artifacts["DockBinderFrcmod"])
        ref_lig_frcmod = self.work_dir / in_ref_frcmod.name
        shutil.copy(in_ref_frcmod, ref_lig_frcmod)
        #
        in_tgt_frcmod = Path(self.input_artifacts["LigandFrcmod"])
        tgt_lig_frcmod = self.work_dir / in_tgt_frcmod.name
        shutil.copy(in_tgt_frcmod, tgt_lig_frcmod)

        # lib files
        in_ref_lib = Path(self.input_artifacts["DockBinderLib"])
        ref_lig_lib = self.work_dir / in_ref_lib.name

        in_tgt_lib = Path(self.input_artifacts["LigandLib"])
        tgt_lig_lib = self.work_dir / in_tgt_lib.name

        ref_lig_pdb = self.init_lig_params(
            in_ref_lib,
            Path(self.input_artifacts["BaseDockBinderStructureFile"]),
            resname=self.RESNAME_LIG["reference"],
            out_lig_lib=ref_lig_lib,
        )
        tgt_lig_pdb = self.init_lig_params(
            in_tgt_lib,
            Path(self.input_artifacts["BinderLigandPDB"]),
            resname=self.RESNAME_LIG["target"],
            out_lig_lib=tgt_lig_lib,
        )
        self.node_logger.info(f"Patching {tgt_lig_pdb} using {tgt_lig_lib}")
        patch_pdb_lib(tgt_lig_pdb, tgt_lig_lib, tgt_lig_pdb, tgt_lig_lib, logger=self.node_logger)

        lig_libs = {key: lib for key, lib in zip(self.RESNAME_LIG.keys(), (ref_lig_lib, tgt_lig_lib))}
        cc_atoms_both = self.get_selection(lig_libs)
        lig_pdbs = {key: lib for key, lib in zip(self.RESNAME_LIG.keys(), (ref_lig_pdb, tgt_lig_pdb))}
        self.aligner(lig_libs, lig_pdbs, cc_atoms_both)
        sc_atoms_both = self.get_sc_atoms(lig_libs, cc_atoms_both)
        afe_masks = self.build_masks(sc_atoms_both, cc_atoms_both)

        cc1_atoms, sc1_atoms, cc2_atoms, sc2_atoms = self.build_atom_lists(lig_pdbs, cc_atoms_both, sc_atoms_both)

        if self.rebuild_sc:
            self.delete_sc(lig_pdbs, str(afe_masks["sc2"]))
        self.node_logger.info(
            f"Concatenating {lig_pdbs['reference'].name}, {lig_pdbs['target'].name}, "
            f"{self.input_artifacts['BaseDockTargetStructureFile']}"
        )
        out_complex_pdb = self.work_dir / "dockcomplex.pdb"
        concatenate_pdbs(
            [lig_pdbs["reference"], lig_pdbs["target"], self.input_artifacts["BaseDockTargetStructureFile"]],
            out_complex_pdb,
        )
        assign_chain_ids(out_complex_pdb, out_complex_pdb)

        self.output_artifacts = self.fill_output_artifacts(
            sysname,
            complex_pdb=out_complex_pdb,
            ref_lig_lib=ref_lig_lib,
            ref_lig_frcmod=ref_lig_frcmod,
            tgt_lig_lib=tgt_lig_lib,
            tgt_lig_frcmod=tgt_lig_frcmod,
            box=box,
            afe_masks=afe_masks,
            cc1_atoms=cc1_atoms,
            sc1_atoms=sc1_atoms,
            cc2_atoms=cc2_atoms,
            sc2_atoms=sc2_atoms,
        )

        return self.output_artifacts

    # noinspection DuplicatedCode
    def build_atom_lists(
        self,
        lig_pdbs: dict[str, filepath_t],
        cc_atoms_both: dict[str, tuple[str, ...]],
        sc_atoms_both: dict[str, tuple[str, ...]],
    ) -> tuple[CC1Atomlist, SC1Atomlist, CC2Atomlist, SC2Atomlist]:
        tmp_pdb = self.work_dir / "tmp_complex.pdb"
        concatenate_pdbs(
            [lig_pdbs["reference"], lig_pdbs["target"], self.input_artifacts["BaseDockTargetStructureFile"]],
            tmp_pdb,
        )
        assign_chain_ids(tmp_pdb, tmp_pdb)
        self.node_logger.info(f"Building {tmp_pdb} SC and CC atom lists for both ligands.")

        u = runiverse(tmp_pdb)

        def get_select(uni: mda.Universe, resname: str, atomnames: tuple[str, ...]) -> mda.core.groups.AtomGroup:
            sc_sel_str = f"resname {resname} and name {' '.join(atomnames)}"
            return uni.select_atoms(sc_sel_str)

        ref_or_tgt = "reference"

        mda_cc1_atoms = get_select(u, self.RESNAME_LIG[ref_or_tgt], cc_atoms_both[ref_or_tgt])
        cc1_atoms = CC1Atomlist.from_mda_atoms(mda_cc1_atoms)
        self.node_logger.info(f"Reference CC1 atoms:\n{cc1_atoms}")

        mda_sc1_atoms = get_select(u, self.RESNAME_LIG[ref_or_tgt], sc_atoms_both[ref_or_tgt])
        sc1_atoms = SC1Atomlist.from_mda_atoms(mda_sc1_atoms)
        self.node_logger.info(f"Reference SC1 atoms:\n{sc1_atoms}")

        ref_or_tgt = "target"
        mda_cc2_atoms = get_select(u, self.RESNAME_LIG[ref_or_tgt], cc_atoms_both[ref_or_tgt])
        cc2_atoms = CC2Atomlist.from_mda_atoms(mda_cc2_atoms)
        self.node_logger.info(f"Target CC2 atoms:\n{cc2_atoms}")

        mda_sc2_atoms = get_select(u, self.RESNAME_LIG[ref_or_tgt], sc_atoms_both[ref_or_tgt])
        sc2_atoms = SC2Atomlist.from_mda_atoms(mda_sc2_atoms)
        self.node_logger.info(f"Target SC2 atoms:\n{sc2_atoms}")

        return cc1_atoms, sc1_atoms, cc2_atoms, sc2_atoms

    def get_sc_atoms(
        self, lig_libs: dict[str, filepath_t], cc_atoms_both: dict[str, tuple[str, ...]]
    ) -> dict[str, tuple[str, ...]]:
        sc_atoms: dict[str, tuple[str, ...]] = {}
        for ref_or_tgt, lig_lib in lig_libs.items():
            lig = parmed.load_file(str(lig_lib))
            # noinspection PyUnresolvedReferences
            lig_residue_template = next(iter(lig.values()))
            set_cc_atoms = set(cc_atoms_both[ref_or_tgt])
            # noinspection PyUnresolvedReferences
            sc_atoms_ref_or_tgt = tuple(
                [atom.name for atom in lig_residue_template.atoms if atom.name not in set_cc_atoms]
            )
            if len(sc_atoms_ref_or_tgt) == 0:
                err_msg = f"Found no SC atoms on {ref_or_tgt}. Atoms: {lig_residue_template} CC atoms: {set_cc_atoms}"
                self.node_logger.error(err_msg)
                raise WorkNodeRunningError(err_msg)

            sc_atoms[ref_or_tgt] = sc_atoms_ref_or_tgt
            self.node_logger.info(f"{lig_lib} ligand SC atoms:\n{sc_atoms_ref_or_tgt}")
        return sc_atoms

    def build_masks(
        self, sc_atoms_both: dict[str, tuple[str, ...]], cc_atoms_both: dict[str, tuple[str, ...]]
    ) -> dict[str, BaseAmberMaskString]:
        """Build soft-core masks for the target ligand based on common-core atom names.
        I could just negate the common-core mask, but I want the masks to look nicer.
        """
        afe_masks: dict[str, BaseAmberMaskString] = {}
        for ref_or_tgt, sc_atoms in sc_atoms_both.items():
            cc_atoms = cc_atoms_both[ref_or_tgt]
            cc_mask_str = f":{self.RESNAME_LIG[ref_or_tgt]}@" + ",".join([at for at in cc_atoms])
            sc_mask_str = f":{self.RESNAME_LIG[ref_or_tgt]}@" + ",".join([at for at in sc_atoms])
            if ref_or_tgt == "reference":
                afe_masks["cc1"] = AmberTI1Mask(self.MASK_LIG["reference"])
                afe_masks["sc1"] = AmberSC1Mask(sc_mask_str)
            else:
                afe_masks["cc2"] = AmberTI2Mask(self.MASK_LIG["target"])
                afe_masks["sc2"] = AmberSC2Mask(sc_mask_str)

            self.node_logger.info(
                f"Common-core atom selection mask for the {ref_or_tgt}:\n{cc_mask_str}\nSoft-core atom mask:\n{sc_mask_str}"
            )

        return afe_masks

    # noinspection PyUnresolvedReferences
    def delete_sc(
        self,
        lig_pdbs: dict[str, filepath_t],
        sc_mask: str,
    ) -> None:
        self.node_logger.info("Deleting soft-core atoms.")

        tgt_pdb = parmed.load_file(str(lig_pdbs["target"]))
        sc_selection = parmed.amber.AmberMask(tgt_pdb, sc_mask)
        sc_atoms = ";".join([f"{tgt_pdb[idx].number} {tgt_pdb[idx].name}" for idx in sc_selection.Selected()])
        self.node_logger.info(f"Will strip the following soft-core atoms from target ligand:\n{sc_atoms}")

        tgt_pdb.strip(sc_mask)
        backup_pdb = self.work_dir / ("sc_" + lig_pdbs["target"].name)
        shutil.copy(lig_pdbs["target"], backup_pdb)
        self.node_logger.info(f"Backed up original target ligand to {backup_pdb} Overwriting {lig_pdbs['target']}")

        tgt_pdb.save(str(lig_pdbs["target"]), overwrite=True)

    def rmsdcommoncore(
        self,
        lig_libs: dict[str, filepath_t],
        lig_pdbs: dict[str, filepath_t],
        cc_atoms_both: dict[str, tuple[str, ...]],
    ) -> None:
        self.node_logger.info("Will use both RMSD and commoncore alignment methods.")
        self.rmsd(lig_libs, lig_pdbs, cc_atoms_both)
        self.commoncore(lig_libs, lig_pdbs, cc_atoms_both)

    # noinspection PyUnusedLocal, PyUnresolvedReferences
    def commoncore(
        self,
        lig_libs: dict[str, filepath_t],
        lig_pdbs: dict[str, filepath_t],
        cc_atoms_both: dict[str, tuple[str, ...]],
    ) -> None:
        self.node_logger.info("Assigning reference CC atoms coordinates to the target's")
        ref_in = parmed.load_file(str(lig_pdbs["reference"]))
        tgt_in = parmed.load_file(str(lig_pdbs["target"]))

        ref_atoms_map = {atom.name: atom for atom in ref_in.view[f":{self.RESNAME_LIG['reference']}"].atoms}
        tgt_atoms_map = {atom.name: atom for atom in tgt_in.view[f":{self.RESNAME_LIG['target']}"].atoms}

        for ref_name, tgt_name in cc_atoms_both["ref_to_tgt"].items():
            assert ref_name in ref_atoms_map, f"Reference atom '{ref_name}' not found in {ref_atoms_map}"
            assert tgt_name in tgt_atoms_map, f"Reference atom '{ref_name}' not found in {ref_atoms_map}"
            ref_atom = ref_atoms_map[ref_name]
            tgt_atom = tgt_atoms_map[tgt_name]
            tgt_atom.xx = ref_atom.xx
            tgt_atom.xy = ref_atom.xy
            tgt_atom.xz = ref_atom.xz

        self.node_logger.info(f"Overwriting {lig_pdbs['target']} with aligned coordinates.")
        tgt_in.save(str(lig_pdbs["target"]), overwrite=True)

    # noinspection PyUnusedLocal
    def rmsd(
        self,
        lig_libs: dict[str, filepath_t],
        lig_pdbs: dict[str, filepath_t],
        cc_atoms_both: dict[str, Any],
    ) -> None:
        self.node_logger.info("Using MDAnalysis' RMSD method to align the target ligand to the reference ligand")

        def build_selection_string(atom_names: Any, mol: str) -> str:
            # Chlorine atoms in PDB files are named "Cl", but MDAnalysis expects "CL"
            upper_names_str = ""
            lower_names_str = ""
            for name in atom_names:
                upper_names_str += name.upper() + " "
                lower_names_str += name[0] + name[1:].lower() + " "
            upper_atomsel = f"resname {self.RESNAME_LIG[mol]} and name {upper_names_str}"
            lower_atomsel = f"resname {self.RESNAME_LIG[mol]} and name {lower_names_str}"
            full_atomsel = f"({upper_atomsel}) or ({lower_atomsel})"
            return full_atomsel

        atoms_to_align = {}
        universes = {}
        for ref_or_tgt, lig_pdb in lig_pdbs.items():
            selmask = build_selection_string(cc_atoms_both[ref_or_tgt], ref_or_tgt)
            self.node_logger.info(f"MDAnalysis selection mask for {ref_or_tgt}:\n {selmask}")
            u = runiverse(lig_pdb)
            universes[ref_or_tgt] = u
            atoms_to_align[ref_or_tgt] = u.select_atoms(selmask)

        atom_counts = [len(an) for an in atoms_to_align.values()]
        if len(set(atom_counts)) != 1:
            err_msg = (
                f"Reference selection:\n{cc_atoms_both['reference']}\ngave:\n{atoms_to_align['reference']}\nand "
                f"target selection:\n{cc_atoms_both['target']} gave:\n{atoms_to_align['target']}.\n"
                f"The selections have different atom counts {atom_counts}, they must have the same number of atoms."
            )
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)
        # Set `tol_mass` to 99 to ignore different elements when doing the alignment.
        analysis.align.alignto(atoms_to_align["target"], atoms_to_align["reference"], tol_mass=99)

        self.node_logger.info(f"Overwriting {lig_pdbs['target']} with aligned coordinates.")
        wuniverse(universes["target"], lig_pdbs["target"])

    # noinspection PyUnresolvedReferences
    def init_lig_params(
        self,
        lig_lib: filepath_t,
        lig_pdb: filepath_t,
        *,
        resname: str,
        out_lig_lib: filepath_t,
    ) -> Path:
        # lib
        p = parmed.amber.offlib.AmberOFFLibrary.parse(str(lig_lib))
        key = [k for k in p][0]
        p[resname] = p[key]
        p[resname].name = resname
        del p[key]
        parmed.amber.offlib.AmberOFFLibrary.write(p, str(out_lig_lib))

        # pdb
        u = runiverse(lig_pdb)
        ligatoms = u.select_atoms(f"resname {key}")
        if len(ligatoms) == 0:
            err_msg = f"Input lib {lig_lib} has resname {key}, but input pdb {lig_pdb} does not have any atoms with that resname."
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)
        for res in ligatoms.residues:
            res.resname = resname
        out_lig_pdb = self.work_dir / f"{lig_pdb.stem}_{resname}.pdb"
        wuniverse(u, out_lig_pdb)

        return out_lig_pdb

    def get_selection(self, lig_libs: dict[str, filepath_t]) -> dict[str, Any]:
        atom_names = self.selector(lig_libs["reference"], lig_libs["target"])
        if atom_names["reference"] is None or atom_names["target"] is None:
            err_msg = (
                f'Either the reference lib ({lig_libs["reference"]}) or target lib (lig_libs["target"]) "'
                "failed the selection of common atoms."
            )
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)

        atom_counts = [len(an) for an in atom_names.values()]
        if len(set(atom_counts)) != 1:
            err_msg = f"Could not find the same amide atoms in both ligands. Found: {atom_names}"
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)

        self.node_logger.info(
            f"Selecting {atom_counts[0]} reference atoms for alignment:\n{atom_names['reference']}"
            f"\nAnd {atom_counts[1]} target atoms:\n{atom_names['target']}"
        )
        atom_names["ref_to_tgt"] = {r: t for r, t in zip(atom_names["reference"], atom_names["target"])}
        self.node_logger.info(f"The reference to target atom name mapping is:\n{atom_names['ref_to_tgt']}")

        atom_names["tgt_to_ref"] = {t: r for r, t in zip(atom_names["reference"], atom_names["target"])}
        self.node_logger.info(f"The target to reference atom name mapping is:\n{atom_names['tgt_to_ref']}")

        return atom_names

    def mcs(self, ref_lib, tgt_lib) -> dict[str, Any]:
        self.node_logger.info(f"Using MCS selector to find common atoms between {ref_lib.name} and {tgt_lib.name}")

        def _mcs(ref_pdb: Path, tgt_pdb: Path) -> dict[str, tuple[str, ...]]:
            """
            Finds the maximum common substructure (MCS) between two molecules and returns the atom names

            Parameters
            ----------
            ref_pdb : Path
                Filepath for the reference MOL2 file.
            tgt_pdb : Path
                Filepath for the target MOL2 file.

            Returns
            -------
            dict[str, tuple[str, ...]]
                A list of atom names from the reference molecule that are part of the MCS.
                Returns an empty list if an error occurs or no MCS is found.
            """
            names = {}
            ref_mol = Chem.MolFromPDBFile(str(ref_pdb), removeHs=False)
            tgt_mol = Chem.MolFromPDBFile(str(tgt_pdb), removeHs=False)

            mcs_result = rdFMCS.FindMCS([ref_mol, tgt_mol], timeout=10)
            if mcs_result.numAtoms == 0:
                return names
            mcs_mol = Chem.MolFromSmarts(mcs_result.smartsString)
            if not mcs_mol:
                return names

            ref_match_indices = ref_mol.GetSubstructMatch(mcs_mol)
            tgt_match_indices = tgt_mol.GetSubstructMatch(mcs_mol)

            if not ref_match_indices or not tgt_match_indices:
                return names

            # Get atom names
            names["reference"] = tuple(
                [
                    ref_mol.GetAtomWithIdx(atom_idx).GetPDBResidueInfo().GetName().strip()
                    for atom_idx in ref_match_indices
                ]
            )
            names["target"] = tuple(
                [
                    tgt_mol.GetAtomWithIdx(atom_idx).GetPDBResidueInfo().GetName().strip()
                    for atom_idx in tgt_match_indices
                ]
            )

            return names

        pmd_ref = parmed.amber.offlib.AmberOFFLibrary.parse(str(ref_lib))
        rt_ref = pmd_ref[self.RESNAME_LIG["reference"]]
        tmp_ref = self.work_dir / "tmp_ref.pdb"
        rt_ref.save(str(tmp_ref), overwrite=True)

        pmd_tgt = parmed.amber.offlib.AmberOFFLibrary.parse(str(tgt_lib))
        rt_tgt = pmd_tgt[self.RESNAME_LIG["target"]]
        tmp_tgt = self.work_dir / "tmp_tgt.pdb"
        rt_tgt.save(str(tmp_tgt), overwrite=True)

        atom_names = _mcs(tmp_ref, tmp_tgt)
        return atom_names

    def amide(self, ref_lib, tgt_lib) -> dict[str, Any]:
        self.node_logger.info(f"Using amide selector to find common atoms between {ref_lib.name} and {tgt_lib.name}")

        def _amide(lib_residue_template) -> Optional[tuple[str, ...]]:
            """
            Determines if the residue contains an amide group, and returns the names of the amide atoms.

            An amide group is defined by the following specific criteria:
            1. A **carbonyl carbon** atom whose type starts with 'c'.
            2. This carbon must be bonded to at least three other atoms.
            3. One of its bonded partners must be a **nitrogen** atom of type 'ne' or 'nf',
               which itself must be bonded to at least one other atom besides the carbonyl carbon.
            4. Another of its bonded partners must be a **carbonyl oxygen** atom whose type
               starts with 'o', and this oxygen must ONLY be bonded to the carbonyl carbon.

            Returns
            -------
            dict[str, str]
                The names of the amide atoms if the amide is found, empty otherwise.
            """

            names = {}
            for carbon_candidate in lib_residue_template.atoms:
                if carbon_candidate.type.startswith("c") and len(carbon_candidate.bond_partners) > 2:
                    nitrogen = ""
                    oxygen = ""
                    for partner in carbon_candidate.bond_partners:
                        if partner.type in ("ne", "nf") and len(partner.bond_partners) > 1:
                            nitrogen = partner.name
                        elif partner.type.startswith("o") and len(partner.bond_partners) == 1:
                            oxygen = partner.name

                    # If we found both required partners for this carbon, we're done.
                    if nitrogen != "" and oxygen != "":
                        names["carbon"] = carbon_candidate.name
                        names["nitrogen"] = nitrogen
                        names["oxygen"] = oxygen
                        return tuple(names.values())
            return None

        ref_res_template = parmed.amber.offlib.AmberOFFLibrary.parse(str(ref_lib))[self.RESNAME_LIG["reference"]]
        tgt_res_template = parmed.amber.offlib.AmberOFFLibrary.parse(str(tgt_lib))[self.RESNAME_LIG["target"]]
        atom_names = {"reference": _amide(ref_res_template), "target": _amide(tgt_res_template)}
        return atom_names

    def amideplus(self, ref_lib, tgt_lib) -> dict[str, Any]:
        self.node_logger.info(f"Using selector aligner to find common atoms between {ref_lib.name} and {tgt_lib.name}")

        def _amideplus(residue_template) -> Optional[tuple[str, ...]]:
            """
            Identifies a specific conserved substructure within a residue template.

            The substructure is defined by a central amide group linked to a thiazole-like
            ring on one side and a branched carbon chain on the other.

            It searches for the following pattern:


                C_gamma1   O_carbonyl   ring_N -- C_alpha -- S
                   |          ||          |           |
                C_beta --- C_carbonyl -- anchor_N ----+
                   |
                C_gamma2

            Returns
            -------
            Optional[dict[str, str]]
                A dictionary mapping descriptive keys to the atom names if the full
                substructure is found, otherwise None.
            """
            # 1. Find the unique anchor nitrogen atom ('ne' or 'nf'). This is our starting point.
            anchor_nitrogens = [atom for atom in residue_template.atoms if atom.type.lower() in ("ne", "nf")]
            if len(anchor_nitrogens) != 1:
                return None
            anchor_n = anchor_nitrogens[0]

            # 2. The anchor nitrogen must be bonded to exactly two carbons
            carbon_partners = [p for p in anchor_n.bond_partners if p.type.lower().startswith("c")]
            if len(carbon_partners) != 2:
                return None

            # 3. Distinguish the two carbons: one is bonded to a sulfur ('ss'), the other is not
            c_alpha = None
            c_carbonyl = None
            for c in carbon_partners:
                if any(p.type.lower() == "ss" for p in c.bond_partners):
                    c_alpha = c
                else:
                    c_carbonyl = c

            if not c_alpha or not c_carbonyl:
                return None  # Failed to find both required carbon types.

            # 4. Find atoms connected to the carbonyl carbon: the anchor_n, an oxygen, and another carbon (c_beta)
            carbonyl_partners = c_carbonyl.bond_partners
            if len(carbonyl_partners) != 3:
                return None

            o_carbonyl_list = [p for p in carbonyl_partners if p.type.lower().startswith("o")]
            c_beta_list = [p for p in carbonyl_partners if p.type.lower().startswith("c") and p != anchor_n]

            if not (len(o_carbonyl_list) == 1 and len(c_beta_list) == 1):
                return None
            o_carbonyl = o_carbonyl_list[0]
            c_beta = c_beta_list[0]

            # 5. The alpha-carbon should be bonded to anchor_n, a sulfur ('ss'), and another nitrogen
            alpha_partners = c_alpha.bond_partners
            if len(alpha_partners) < 3:  # Can be > 3 if part of a fused ring system
                return None

            s_atom_list = [p for p in alpha_partners if p.type.lower() == "ss"]
            n_ring_list = [p for p in alpha_partners if p.type.lower().startswith("n") and p != anchor_n]

            if not (len(s_atom_list) == 1 and len(n_ring_list) == 1):
                return None
            s_atom = s_atom_list[0]
            n_ring = n_ring_list[0]

            # 6. Find the two gamma-carbons attached to c_beta. Its partners should include c_carbonyl and two other carbons.
            c_gamma_list = [p for p in c_beta.bond_partners if p.type.lower().startswith("c") and p != c_carbonyl]
            if len(c_gamma_list) != 2:
                return None

            names = {
                "anchor_nitrogen": anchor_n.name,
                "carbonyl_carbon": c_carbonyl.name,
                "carbonyl_oxygen": o_carbonyl.name,
                "c_alpha": c_alpha.name,
                "c_beta": c_beta.name,
                "sulfur": s_atom.name,
                "ring_nitrogen": n_ring.name,
                "c_gamma1": c_gamma_list[0].name,
                "c_gamma2": c_gamma_list[1].name,
            }

            return tuple(names.values())

        ref_res_template = parmed.amber.offlib.AmberOFFLibrary.parse(str(ref_lib))[self.RESNAME_LIG["reference"]]
        tgt_res_template = parmed.amber.offlib.AmberOFFLibrary.parse(str(tgt_lib))[self.RESNAME_LIG["target"]]

        atom_names = {"reference": _amideplus(ref_res_template), "target": _amideplus(tgt_res_template)}
        return atom_names

    def _try_and_skip(self, sysname: str) -> bool:
        raise NotImplementedError

    # noinspection PyMethodMayBeStatic
    def fill_output_artifacts(
        self,
        sysname: str,
        *,
        complex_pdb: Path,
        ref_lig_lib: Path,
        ref_lig_frcmod: Path,
        tgt_lig_lib: Path,
        tgt_lig_frcmod: Path,
        box: BaseComplexPeriodicBox = None,
        afe_masks: dict[str, BaseAmberMaskString],
        cc1_atoms: CC1Atomlist,
        sc1_atoms: SC1Atomlist,
        cc2_atoms: CC2Atomlist,
        sc2_atoms: SC2Atomlist,
    ) -> ArtifactContainer:
        artifacts = [
            DockProteinLigandComplexPDB(complex_pdb),
            DockBinderLib(ref_lig_lib),
            DockBinderFrcmod(ref_lig_frcmod),
            LigandLib(tgt_lig_lib),
            LigandFrcmod(tgt_lig_frcmod),
            box,
            cc1_atoms,
            sc1_atoms,
            cc2_atoms,
            sc2_atoms,
        ]

        return ArtifactContainer(sysname, artifacts + list(afe_masks.values()))
