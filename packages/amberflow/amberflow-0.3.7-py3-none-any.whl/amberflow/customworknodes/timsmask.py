import warnings
from logging import Logger
from typing import Any, Optional, Union

import MDAnalysis as mda
import networkx as nx
import numpy as np
from MDAnalysis.lib import distances

from amberflow.artifacts import (
    BasePeriodicBox,
    ArtifactContainer,
    BaseAmberMaskString,
    BaseAtomList,
    BaseComplexTopologyFile,
    BaseComplexStructureFile,
    CC1Atomlist,
    SC1Atomlist,
    SC2Atomlist,
    CC2Atomlist,
    get_biomolecule,
    CartesianRestraintMask,
)
from amberflow.artifacts.md import AmberNMRRestraints
from amberflow.primitives import (
    filepath_t,
    dirpath_t,
    WorkNodeRunningError,
)
from amberflow.worknodes import (
    worknodehelper,
    BaseSingleWorkNode,
    get_molgraph,
)

__all__ = ("DockRestraints",)

AtomPairWithDistance = tuple[mda.core.groups.Atom, mda.core.groups.Atom, float]


@worknodehelper(
    file_exists=True,
    input_artifact_types=(
        BaseComplexTopologyFile,
        BaseComplexStructureFile,
        BaseAtomList,
        BaseAmberMaskString,
    ),
    optional_artifact_types=(BasePeriodicBox,),
    need_all_input_artifacts=False,
    output_artifact_types=(
        AmberNMRRestraints,
        CartesianRestraintMask,
    ),
)
class DockRestraints(BaseSingleWorkNode):
    """ """

    RESNAME_LIG: dict[str, str] = {"reference": "L00", "target": "L01"}
    MAX_CUTOFF: float = 10.0

    def __init__(
        self,
        wnid: str,
        *args,
        cc_contacts_cutoff: float = 3,
        min_cc_contacts: int = 4,
        cc_contacts_step_size: float = 0.1,
        sc_contacts_nofreeze_cutoff: float = 3,
        force_amide_arg_contact: bool = True,
        force_amide_ser_contact: bool = True,
        force_thiadiazole_arg_contact: bool = True,
        force_exclude_after_thiadiazole: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            wnid=wnid,
            *args,
            **kwargs,
        )
        self.cc_contacts_cutoff = cc_contacts_cutoff
        self.min_cc_contacts = min_cc_contacts
        self.cc_contacts_step_size = cc_contacts_step_size
        self.sc_contacts_nofreeze_cutoff = sc_contacts_nofreeze_cutoff
        self.force_amide_arg_contact = force_amide_arg_contact
        self.force_amide_ser_contact = force_amide_ser_contact
        self.force_thiadiazole_arg_contact = force_thiadiazole_arg_contact
        self.force_exclude_after_thiadiazole = force_exclude_after_thiadiazole

    def _run(
        self,
        *,
        cwd: dirpath_t,
        sysname: str,
        binpath: Optional[filepath_t] = None,
        **kwargs,
    ) -> Any:
        biomol = get_biomolecule(self.input_artifacts, self.node_logger)
        self.node_logger.info(f"Working with {biomol}")

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            u = mda.Universe(
                self.input_artifacts["ComplexProteinLigandTopology"],
                self.input_artifacts["ComplexProteinLigandRestart"],
                format="RESTRT",
            )
        cc_contacts, sc_contacts = self.get_all_contacts(
            u,
            self.input_artifacts["CC1Atomlist"],
            self.input_artifacts["CC2Atomlist"],
            self.input_artifacts["SC1Atomlist"],
            self.input_artifacts["SC2Atomlist"],
        )

        if self.force_amide_arg_contact:
            self.node_logger.info("Forcing amide-ARG contact restraints")
            target_selection = "resname ARG and element N"
            target_atoms = u.select_atoms(target_selection)
            for resname in self.RESNAME_LIG.values():
                _, _, n = self.find_amide(u, resname)
                contact = self.get_contact(target_atoms, n)
                cc_contacts.append(contact)
        if self.force_amide_ser_contact:
            self.node_logger.info("Forcing amide-SER contact restraints")
            target_selection = "resname SER and element O"
            target_atoms = u.select_atoms(target_selection)
            for resname in self.RESNAME_LIG.values():
                _, o, _ = self.find_amide(u, resname)
                contact = self.get_contact(target_atoms, o)
                cc_contacts.append(contact)
        if self.force_thiadiazole_arg_contact:
            self.node_logger.info("Forcing thiadiazole-ARG contact restraints")
            target_selection = "resname ARG and element N"
            target_atoms = u.select_atoms(target_selection)
            for resname in self.RESNAME_LIG.values():
                c20, n4, n5, c19, s1 = self.find_thiadiazole(u, resname)
                contact = self.get_contact(target_atoms, n5)
                cc_contacts.append(contact)
        if self.force_exclude_after_thiadiazole:
            self.node_logger.info("Excluding contacts after thiadiazole")
            new_cc_contacts = []
            for resname in self.RESNAME_LIG.values():
                c20, n4, n5, c19, s1 = self.find_thiadiazole(u, resname)
                atomos = u.select_atoms(f"resname {resname}")
                molgraph = get_molgraph(atomos, c19)
                to_exclude = self.dfs_from_root_with_exclusions(
                    molgraph, root=c19.index, exclude=(s1.index, n4.index), logger=self.node_logger
                )

                for par in cc_contacts:
                    if par[0].name in to_exclude or par[1].name in to_exclude:
                        self.node_logger.info(f"Excluding contact {par} because of after-thiadiazole exclusion")
                        continue
                    new_cc_contacts.append(par)
            cc_contacts = new_cc_contacts

        self.node_logger.info(self.format_interaction_results(cc_contacts))
        cc_restraints = AmberNMRRestraints.write_disang_from_mda_atoms(
            self.work_dir, restraint_data=cc_contacts, restraint_strength=50, restraint_type="halfharmonic"
        )
        self.node_logger.info(f"Wrote NMR restraints to {cc_restraints}")

        ntr_mask = self.build_target_restraint_mask(u, sc_contacts, biomol)
        self.node_logger.info(f"Using restraint mask: {ntr_mask}")

        self.output_artifacts = self.fill_output_artifacts(
            sysname,
            ntr_mask=ntr_mask,
            cc_restraints=cc_restraints,
        )

        return self.output_artifacts

    # def remove_contacts_after(self, u: mda.Universe, resname: str, cc_contacts: list[AtomPairWithDistance], liminal_atoms: tuple[mda.core.groups.Atom, ...]) ->list[AtomPairWithDistance]:

    def build_target_restraint_mask(
        self, u: mda.Universe, sc_contacts: list[AtomPairWithDistance], biomol: str
    ) -> CartesianRestraintMask:
        target_residues = u.select_atoms(biomol).residues
        if len(target_residues) == 0:
            err_msg = f"No residues found with selection: {biomol}"
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)
        resids = target_residues.resids
        min_resid = resids.min()
        max_resid = resids.max()
        # Assuming it's a continuous range:
        target_mask = CartesianRestraintMask(f"(:{min_resid}-{max_resid})")

        # ignore hydrogens and solvent
        target_mask += "&(!@H=)&(!:NA,CL,MG,WAT)"

        # `sc_contacts` should be free to move
        all_indices = set([str(par[0].index) for par in sc_contacts] + [str(par[1].index) for par in sc_contacts])
        free_indices = "@" + ",".join(all_indices)
        target_mask += f"&(!{free_indices})"

        return target_mask

    @staticmethod
    def find_amide(u: mda.Universe, resname: str) -> Union[tuple[Any, Any, Any], None]:
        lig_o = u.select_atoms(f"resname {resname} and element O")
        for o in lig_o:
            if len(o.bonds) == 1:
                for obonds in o.bonds:
                    for candidate_carbonyl in obonds:
                        if candidate_carbonyl.element == "C":
                            for cbonds in candidate_carbonyl.bonds:
                                for candidate_nitrogen in cbonds:
                                    if candidate_nitrogen.type in ("ne", "nf"):
                                        return candidate_carbonyl, o, candidate_nitrogen
        return None

    # noinspection PyTypeChecker
    @staticmethod
    def find_thiadiazole(u: mda.Universe, resname: str) -> Union[Any, None]:
        ccarbonyl, _, n_amide = DockRestraints.find_amide(u, resname)
        ring = dict.fromkeys(["c19", "c20", "n4", "n5", "s1"])
        for b in n_amide.bonds:
            ring_carbon = b[1] if b[0].id == n_amide.id else b[0]
            if ring_carbon.id == ccarbonyl.id:
                continue
            ring["c20"] = ring_carbon
            for bb in ring_carbon.bonds:
                ring_n_or_s = bb[1] if bb[0].id == ring_carbon.id else bb[0]
                if ring_n_or_s.element == "S":
                    ring["s1"] = ring_n_or_s
                    for bbb in ring_n_or_s.bonds:
                        ring_c = bbb[1] if bbb[0].id == ring_n_or_s.id else bbb[0]
                        if ring_c.id != ring_carbon.id:
                            ring["c19"] = ring_c
                elif ring_n_or_s.element == "N":
                    ring["n5"] = ring_n_or_s
                    for bbbb in ring_n_or_s.bonds:
                        ring_n = bbbb[1] if bbbb[0].id == ring_n_or_s.id else bbbb[0]
                        if ring_n.element == "N":
                            ring["n4"] = ring_n
                else:
                    raise WorkNodeRunningError(
                        f"Could not parse thiadiazole ring. Expected S or N, found: {ring_n_or_s}"
                    )
        return ring["c20"], ring["n4"], ring["n5"], ring["c19"], ring["s1"]

    def get_contact(
        self, target_atoms: mda.core.groups.AtomGroup, ligand_atom: mda.core.groups.Atom
    ) -> AtomPairWithDistance:
        dist_matrix = distances.distance_array(ligand_atom.position, target_atoms.positions)
        closest_n = np.argmin(dist_matrix)
        dist = float(dist_matrix[0, closest_n])
        ref_dist = AtomPairWithDistance((target_atoms[closest_n], ligand_atom, dist))

        # these constraint are forced, we didn't set a cutoff, so instead we print the distance
        self.node_logger.info(self.format_interaction_results([ref_dist], ref_dist[2]))
        return ref_dist

    def get_all_contacts(
        self,
        u: mda.Universe,
        cc1_atoms: CC1Atomlist,
        cc2_atoms: CC2Atomlist,
        sc1_atoms: SC1Atomlist,
        sc2_atoms: SC2Atomlist,
    ) -> tuple[list[AtomPairWithDistance], list[AtomPairWithDistance]]:
        cc_contacts: list[AtomPairWithDistance] = []
        for cc_atoms in (cc1_atoms, cc2_atoms):
            self.node_logger.info(
                f"Finding ligand CC atoms and protein atoms within {self.cc_contacts_cutoff}A and increasing by "
                f"{self.cc_contacts_step_size} until finding {self.min_cc_contacts} pairs."
            )
            cc_contacts.extend(
                self.get_contacts(
                    u,
                    cc_atoms,
                    cutoff=self.cc_contacts_cutoff,
                    hydrogens=False,
                )
            )
        sc_contacts: list[AtomPairWithDistance] = []
        for sc_atoms in (sc1_atoms, sc2_atoms):
            self.node_logger.info(
                f"Finding reference ligand SC1 atoms and protein atoms within {self.sc_contacts_nofreeze_cutoff}A"
            )

            sc_contacts.extend(
                self.get_contacts(
                    u,
                    sc_atoms,
                    cutoff=self.sc_contacts_nofreeze_cutoff,
                )
            )

        return cc_contacts, sc_contacts

    def get_contacts(
        self,
        u: mda.Universe,
        atomlist: BaseAtomList,
        cutoff: float,
        hydrogens: bool = True,
    ) -> list[AtomPairWithDistance]:
        """Get and log the number of contacts between the common-core atoms of the reference and target ligands.

        Parameters
        ----------
        u : mda.Universe,
            The path to the complex PDB file containing both ligands.
        atomlist: BaseAtomList
            atom names
        cutoff : float
            The distance cutoff (in Angstroms) to consider a contact.
        hydrogens : bool
            Whether to include hydrogen atoms in the selection.
        """
        not_hydrogens = "" if hydrogens else " and not type H*"
        protein_selection_str = f"protein{not_hydrogens}"
        protein_heavy_atoms = u.select_atoms(protein_selection_str)
        self.node_logger.info(
            f"Found {len(protein_heavy_atoms)} protein atoms with selection:\n{protein_selection_str}"
        )

        ligand_selection_str = atomlist.mda_sel(hydrogens=hydrogens)
        ligand_heavy_atoms = u.select_atoms(ligand_selection_str)
        self.node_logger.info(f"Found {len(ligand_heavy_atoms)} ligand atoms with selection:\n{ligand_selection_str}")

        if len(ligand_heavy_atoms) == 0:
            err_msg = f"No ligand atoms found with selection: '{ligand_selection_str}'"
            self.node_logger.error(err_msg)

        dist_matrix = distances.distance_array(protein_heavy_atoms.positions, ligand_heavy_atoms.positions)
        while True:
            close_indices = np.where(dist_matrix <= cutoff)
            if len(close_indices[0]) < self.min_cc_contacts:
                cutoff += self.cc_contacts_step_size
            else:
                break
            if cutoff > self.MAX_CUTOFF:
                err_msg = (
                    f"Could not find {self.min_cc_contacts} close contacts even with cutoff of {self.MAX_CUTOFF} Å. "
                    f"Found only {len(close_indices[0])} contacts. {ligand_selection_str=}"
                )
                self.node_logger.warning(err_msg)
                return []

        close_pairs: list[AtomPairWithDistance] = [
            (protein_heavy_atoms[i], ligand_heavy_atoms[j], float(dist_matrix[i, j]))
            for i, j in zip(close_indices[0], close_indices[1])
        ]
        self.node_logger.info(self.format_interaction_results(close_pairs, cutoff))
        # close_pairs_names: list[tuple[str, str, float]] = [
        #     (protein_heavy_atoms[i].name, ligand_heavy_atoms[j].name, float(dist_matrix[i, j]))
        #     for i, j in zip(close_indices[0], close_indices[1])
        # ]
        # info_msg = (
        #     f"Found {len(close_pairs_ids)} close contacts (<= {cutoff:.2f} Å) between protein and the reference:\n"
        # )
        # for ids, names in zip(close_pairs_ids, close_pairs_names):
        #     info_msg += f"  Protein atom {ids[0]} ({names[0]})\t-\tLigand atom {ids[1]} ({names[1]})\t:\t{ids[2]:.2f} Å\n"
        # self.node_logger.info(info_msg)
        return close_pairs

    @staticmethod
    def format_interaction_results(
        interaction_pairs: list[AtomPairWithDistance], final_cutoff: Optional[float] = None
    ) -> str:
        """Formats the interaction pairs for logging and PyMOL visualization."""
        if not interaction_pairs:
            return "No interactions found within the cutoff distance."

        def _get_pymol_selection(atom: mda.core.groups.Atom, is_residue_level: bool = False) -> str:
            chain_id = getattr(atom, "chainID", None)

            # Base selection for residue and atom name
            parts = [f"resi {atom.resid}"]
            if not is_residue_level:
                parts.append(f"name {atom.name}")

            # Add chainID only if it exists and is not empty
            if chain_id:
                parts.insert(0, f"chain {chain_id}")

            return f"({' and '.join(parts)})"

        # --- Build the formatted table for logging ---
        extra_msg = "" if final_cutoff is None else f" (cutoff expanded to {final_cutoff:.2f} Å):"
        header = (
            f"Found {len(interaction_pairs)} close contacts{extra_msg}\n\n"
            f"{'Protein Atom':<35} | {'Ligand Atom':<35} | {'Distance (Å)':>12}\n"
            f"{'-' * 35} | {'-' * 35} | {'-' * 12}\n"
        )
        table_rows = []
        for prot_atom, lig_atom, dist in interaction_pairs:
            prot_id = f"{prot_atom.resname}{prot_atom.resid}@{prot_atom.name} (id {prot_atom.id})"
            lig_id = f"{lig_atom.resname}{lig_atom.resid}@{lig_atom.name} (id {lig_atom.id})"
            table_rows.append(f"{prot_id:<35} | {lig_id:<35} | {dist:>12.3f}")

        # --- Build the PyMOL selection strings ---
        prot_residues = {_get_pymol_selection(p_atom, is_residue_level=True) for p_atom, _, _ in interaction_pairs}
        prot_res_selection = " or ".join(sorted(list(prot_residues)))

        unique_lig_atoms = {l for _, l, _ in interaction_pairs}
        lig_atom_selections = [_get_pymol_selection(l_atom) for l_atom in unique_lig_atoms]
        lig_contacts_selection = " or ".join(sorted(lig_atom_selections))

        pymol_commands = [
            "\n\n--- PyMOL Selection Commands ---\n",
            f"select prot_interacting_res, {prot_res_selection}",
            f"select lig_contacts, {lig_contacts_selection}",
            "show sticks, prot_interacting_res or lig_contacts",
            "zoom prot_interacting_res or lig_contacts\n\n",
        ]

        # Create distance objects for each pair
        for i, (p, l, _) in enumerate(interaction_pairs, 1):
            p_selection = _get_pymol_selection(p)
            l_selection = _get_pymol_selection(l)
            pymol_commands.append(f"distance dist{i}, {p_selection}, {l_selection}")

        return header + "\n".join(table_rows) + "\n" + "\n".join(pymol_commands)

    @staticmethod
    def dfs_from_root_with_exclusions(
        graph: nx.Graph, *, root: int, exclude: tuple[int, ...], logger: Optional[Logger] = None
    ) -> set[str]:
        """
        Performs a DFS starting from a root node, excluding specified neighbor branches.

        Args:
            graph: The NetworkX graph to traverse.
            root: The index of the node to start the traversal from.
            exclude: A tuple of atom indices of immediate neighbors of the start node. The traversal will not proceed down these branches.
            logger: Optional logger for logging messages.
        Returns:
            A list of (atom_name, node_index) tuples for all visited nodes.
        """
        if root not in graph:
            err_msg = f"Start node {root} not in the graph."
            if logger:
                logger.error(err_msg)
            raise ValueError(err_msg)

        # Start with the root node's data
        visited = {root}
        start_node_data = graph.nodes[root]
        collected_nodes: list[str] = [start_node_data["atomname"]]

        # Identify the neighbors to start traversing from
        valid_start_points = []
        for neighbor_idx in graph.neighbors(root):
            # neighbor_name = graph.nodes[neighbor_idx].get('atomname')
            if neighbor_idx not in exclude:
                valid_start_points.append(neighbor_idx)

        # Perform DFS from each valid neighbor
        for start_point in valid_start_points:
            if start_point in visited:
                continue
            stack = [start_point]
            while stack:
                current_node_idx = stack.pop()
                if current_node_idx in visited:
                    continue
                visited.add(current_node_idx)
                node_data = graph.nodes[current_node_idx]
                collected_nodes.append(node_data["atomname"])

                for neighbor_idx in reversed(list(graph.neighbors(current_node_idx))):
                    if neighbor_idx not in visited:
                        stack.append(neighbor_idx)

        return set(collected_nodes)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def _try_and_skip(
        self,
        sysname: str,
    ) -> bool:
        return False

    # noinspection PyMethodMayBeStatic
    def fill_output_artifacts(
        self, sysname: str, *, ntr_mask: CartesianRestraintMask, cc_restraints: AmberNMRRestraints
    ) -> ArtifactContainer:
        return ArtifactContainer(sysname, (ntr_mask, cc_restraints))
