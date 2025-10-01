import warnings
from itertools import chain
from pathlib import Path
from typing import Any, Optional

import MDAnalysis as mda
import numpy as np

from amberflow.artifacts.md import (
    BasePeriodicBox,
    BinderLigandPeriodicBox,
    TargetProteinPeriodicBox,
    ComplexProteinLigandPeriodicBox,
    ComplexNucleicLigandPeriodicBox,
    TargetNucleicPeriodicBox,
)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # ignore `BiopythonDeprecationWarning` warning
    from MDAnalysis.analysis import align
    from MDAnalysis.lib.distances import distance_array
from scipy.spatial import KDTree
from scipy.ndimage import distance_transform_edt
from scipy.spatial.transform import Rotation

from amberflow.artifacts import (
    ArtifactContainer,
    BaseBinderLigandStructureFile,
    ArtifactRegistry,
)
from amberflow.customartifacts import BoxBinderLigandPDB
from amberflow.primitives import (
    filepath_t,
    dirpath_t,
)
from amberflow.worknodes import (
    worknodehelper,
    BaseSingleWorkNode,
)

__all__ = ("BoxLigand",)

AtomPairWithDistance = tuple[mda.core.groups.Atom, mda.core.groups.Atom, float]


class BoxGrid:
    """Manages the geometry of a triclinic box and an occupancy grid within it."""

    def __init__(self, box_vectors: np.ndarray, resolution: float):
        self.H = box_vectors
        self.resolution = resolution
        self.dims = np.ceil(np.linalg.norm(self.H, axis=1) / self.resolution).astype(int)
        i, j, k = np.mgrid[0 : self.dims[0], 0 : self.dims[1], 0 : self.dims[2]]
        frac_coords = np.vstack([i.ravel(), j.ravel(), k.ravel()]).T / self.dims
        self.grid_points_cartesian = frac_coords @ self.H
        self.occupancy = np.full(self.grid_points_cartesian.shape[0], False)
        self.kdtree = KDTree(self.grid_points_cartesian)

    def mask_grid_with_atoms(self, atom_coords: np.ndarray, radius: float):
        # noinspection PyTypeChecker
        indices: np.ndarray = self.kdtree.query_ball_point(atom_coords, r=radius)

        if indices.size > 0 and any(len(arr) > 0 for arr in indices):
            occupied_indices = np.unique(np.concatenate(indices)).astype(int)
            self.occupancy[occupied_indices] = True

    def check_clash(self, atom_coords: np.ndarray) -> bool:
        _, closest_indices = self.kdtree.query(atom_coords, k=1)
        return bool(np.any(self.occupancy[closest_indices]))


@worknodehelper(
    file_exists=True,
    input_artifact_types=(
        BaseBinderLigandStructureFile,
        BoxBinderLigandPDB,
    ),
    output_artifact_types=(BaseBinderLigandStructureFile, BasePeriodicBox),
)
class BoxLigand(BaseSingleWorkNode):
    """ """

    RESNAME_LIG: str = "LIG"
    WATER_COORDS = np.array(
        [
            [0.000, 0.000, 0.000],
            [0.757, 0.586, 0.000],
            [-0.757, 0.586, 0.000],
        ]
    )
    WAT_RADIUS = 2.7

    class NoSpaceForWater(Exception):
        pass

    def __init__(
        self,
        wnid: str,
        *args,
        resolution: float = 0.5,
        solute_radius: float = 1.4,
        solvent_radius: float = 1.1,
        clash_cutoff: float = 3,
        **kwargs,
    ) -> None:
        super().__init__(
            wnid=wnid,
            *args,
            **kwargs,
        )

        self.resolution = resolution
        self.solute_radius = solute_radius
        self.solvent_radius = solvent_radius
        self.clash_cutoff = clash_cutoff

    def _run(
        self,
        *,
        cwd: dirpath_t,
        sysname: str,
        binpath: Optional[filepath_t] = None,
        **kwargs,
    ) -> Any:
        in_lig = Path(self.input_artifacts["BaseBinderLigandStructureFile"])
        in_box = Path(self.input_artifacts["BoxBinderLigandPDB"])
        out_pdb = self.work_dir / in_lig.name
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            uin_lig = mda.Universe(in_lig)
            uin_box = mda.Universe(in_box)
        periodic_box = self.get_box(uin_box)

        self.node_logger.info(f"Got box {periodic_box} dimensions and angles:\n{uin_box.dimensions}")

        uin_lig = self.align_intertia_axii(uin_box, uin_lig, f"resname {self.RESNAME_LIG}")
        if not hasattr(uin_lig.atoms, "chainIDs") or np.all(uin_lig.atoms.chainIDs == ""):
            self.node_logger.info(f"No chainIDs found in {in_lig}, assigning 'A'")
            uin_lig.atoms.chainIDs = "A"
        wat_to_add, hollowed_box_atoms = self.clip_waters(
            uin_box,
            uin_lig,
            solvent_sel=f"not resname {self.RESNAME_LIG}",
            solute_sel=f"resname {self.RESNAME_LIG}",
            clash_cutoff=self.clash_cutoff,
        )
        self.node_logger.info(f"Removed {wat_to_add} waters")
        missing_watu = mda.Merge(uin_lig.atoms, hollowed_box_atoms)
        solvated_system = self.add_waters(
            missing_watu, uin_lig, wat_to_add, self.resolution, self.solute_radius, self.solvent_radius
        )
        self.node_logger.info(f"Writing out the solvated ligand to {out_pdb}")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            solvated_system.atoms.write(out_pdb)

        self.output_artifacts = self.fill_output_artifacts(sysname, out_pdb=out_pdb, out_box=periodic_box)

        return self.output_artifacts

    def get_box(self, u: mda.Universe) -> BasePeriodicBox:
        # Make it nicer once this worknode is general for all inputs
        all_tags = set(chain.from_iterable(self.tags.values()))
        if "ligand" in all_tags:
            return BinderLigandPeriodicBox(u.dimensions)
        elif "complex" in all_tags and "protein" in all_tags:
            return ComplexProteinLigandPeriodicBox(u.dimensions)
        elif "complex" in all_tags and "nucleic" in all_tags:
            return ComplexNucleicLigandPeriodicBox(u.dimensions)
        elif "target" in all_tags and "protein" in all_tags:
            return TargetProteinPeriodicBox(u.dimensions)
        elif "target" in all_tags and "nucleic" in all_tags:
            return TargetNucleicPeriodicBox(u.dimensions)
        else:
            err_msg = f"No appropriate tags found. Input artifacts tags: {all_tags}"
            self.node_logger.error(err_msg)
            raise ValueError(err_msg)

    def add_waters(
        self,
        usolvated: mda.Universe,
        uligand: mda.Universe,
        wat_count: int,
        resolution: float = 0.5,
        solute_radius: float = 1.4,
        solvent_radius: float = 1.1,
    ) -> mda.Universe:
        lig_center = uligand.atoms.centroid()
        box_vectors = self.setup_box(uligand)
        box_center = np.diag(box_vectors / 2)

        self.node_logger.info(f"Building gridded box: {box_vectors}")
        b = BoxGrid(box_vectors, resolution)
        b.mask_grid_with_atoms(uligand.atoms.positions - uligand.atoms.centroid(), solute_radius)

        new_wats_coords: np.ndarray
        while solvent_radius > 0.2:
            try:
                new_wats_coords = self.get_wats_coords(
                    usolvated, uligand, wat_count, b, resolution, solvent_radius, lig_center, box_center
                )
            except self.NoSpaceForWater:
                solvent_radius -= 0.1
                self.node_logger.warning(
                    f"Could not place all {wat_count} requested waters. Will try again with {solvent_radius=}"
                )
                continue
            break
        else:
            raise RuntimeError(f"Could not place all {wat_count} waters even with {solvent_radius=}")

        assert len(new_wats_coords) != 0, "Failed to place any waters. This shouldn't happen."
        self.node_logger.info(f"Found coordinates for all replacement waters with {solvent_radius=}")
        solvated_system = self.build_wat_universe(new_wats_coords, usolvated, wat_count)
        solvated_system.dimensions = usolvated.dimensions

        return solvated_system

    @staticmethod
    def build_wat_universe(wat_coords: np.ndarray, usolvated: mda.Universe, wat_count: int) -> mda.Universe:
        water_resnames = np.array(["WAT"] * wat_count)
        water_atom_names = np.array(["O", "H1", "H2"] * wat_count)

        # Create a new Universe for the water and merge
        water_universe = mda.Universe.empty(
            n_atoms=len(wat_coords),
            n_residues=wat_count,
            atom_resindex=np.repeat(np.arange(wat_count), 3),
            trajectory=True,
        )
        water_universe.atoms.positions = wat_coords
        water_universe.add_TopologyAttr("name", water_atom_names)
        water_universe.add_TopologyAttr("resname", water_resnames)
        last_resid = usolvated.residues.resids[-1]
        water_universe.add_TopologyAttr("resid", range(last_resid + 1, last_resid + wat_count + 1))
        chainids = np.repeat("", len(water_universe.atoms))
        water_universe.add_TopologyAttr("chainIDs", chainids)

        solvated_system = mda.Merge(usolvated.atoms, water_universe.atoms)
        return solvated_system

    def get_wats_coords(
        self,
        usolvated: mda.Universe,
        uligand: mda.Universe,
        wat_count: int,
        b: BoxGrid,
        resolution: float = 0.5,
        solvent_radius: float = 1.1,
        lig_center: np.ndarray = None,
        box_center: np.ndarray = None,
    ) -> np.ndarray:
        b.mask_grid_with_atoms(usolvated.atoms.positions - lig_center, solvent_radius)

        placed_solvent_coords = []
        for i in range(wat_count):
            # 1. Reshape the 1D occupancy array into a 3D grid
            occupancy_grid_3d = b.occupancy.reshape(b.dims)

            # 2. Compute the distance transform on the *unoccupied* points
            # The '~' inverts the boolean array, so we find distances from occupied points.
            distance_map = distance_transform_edt(~occupancy_grid_3d)

            # 3. Find the grid index of the largest empty space
            max_dist_idx_flat = np.argmax(distance_map)
            # np.unravel_index converts the flat index back to 3D grid coordinates
            max_dist_idx_3d = np.unravel_index(max_dist_idx_flat, b.dims)

            # 4. Check if the largest space is big enough for a solvent molecule
            # noinspection PyTypeChecker
            if distance_map[max_dist_idx_3d] * resolution < solvent_radius:
                raise self.NoSpaceForWater

            # 5. Get the Cartesian coordinates for the center of this void
            # We need to convert the 3D grid index back to the original 1D index
            # for our pre-calculated grid_points_cartesian array
            placement_center_idx_1d = np.ravel_multi_index(max_dist_idx_3d, b.dims)
            placement_center_cart = b.grid_points_cartesian[placement_center_idx_1d]

            # 6. Place the molecule
            random_rotation = Rotation.random().as_matrix()
            oriented_solvent = BoxLigand.WATER_COORDS @ random_rotation.T
            trial_coords = oriented_solvent + placement_center_cart

            placed_solvent_coords.append(trial_coords + uligand.atoms.centroid() - box_center)
            b.mask_grid_with_atoms(trial_coords, self.WAT_RADIUS + (self.WAT_RADIUS - solvent_radius))

        new_wats_coords = np.vstack(placed_solvent_coords)
        return new_wats_coords

    @staticmethod
    def setup_box(u: mda.Universe) -> np.ndarray:
        x_min, y_min, z_min = np.min(u.atoms.positions, axis=0) - 5
        x_max, y_max, z_max = np.max(u.atoms.positions, axis=0) + 5

        lx = x_max - x_min
        ly = y_max - y_min
        lz = z_max - z_min

        return np.array([[lx, 0, 0], [0, ly, 0], [0, 0, lz]])

    @staticmethod
    def clip_waters(
        uref: mda.Universe, utgt: mda.Universe, *, solvent_sel: str, solute_sel: str, clash_cutoff: float = 3.0
    ) -> tuple[int, mda.core.groups.Atom]:
        solvent_from_box = uref.select_atoms(solvent_sel)
        solute_tgt = utgt.select_atoms(solute_sel)

        dist_matrix = distance_array(solvent_from_box.positions, solute_tgt.positions)
        clashing_indices = np.where(dist_matrix < clash_cutoff)
        clashing_wat_resids = set([solvent_from_box[solvent_idx].resid for solvent_idx in clashing_indices[0]])
        clashing_wat_sele = "resid " + " or resid ".join([str(r) for r in clashing_wat_resids])
        if len(clashing_wat_resids) == 0:
            return 0, uref.atoms
        nonclash_box_atoms = uref.select_atoms(f"not {clashing_wat_sele} and not {solute_sel}")
        clashing_wat_count = len(clashing_wat_resids)

        return clashing_wat_count, nonclash_box_atoms

    @staticmethod
    def align_intertia_axii(uref: mda.Universe, utgt: mda.Universe, selection_str: str) -> mda.Universe:
        ref_selection = uref.select_atoms(selection_str)
        mobile_selection = utgt.select_atoms(selection_str)

        ref_com = ref_selection.center_of_mass()
        ref_pa = ref_selection.principal_axes()  # Eigenvectors of the inertia tensor

        mobile_com = mobile_selection.center_of_mass()
        mobile_pa = mobile_selection.principal_axes()
        utgt.atoms.translate(-mobile_com)

        rot_mtx, _ = align.rotation_matrix(mobile_pa, ref_pa)
        utgt.atoms.rotate(rot_mtx)
        utgt.atoms.translate(ref_com)

        return utgt

    # noinspection DuplicatedCode
    def _try_and_skip(
        self,
        sysname: str,
        *,
        out_pdb: filepath_t,
        out_box: BasePeriodicBox,
    ) -> bool:
        if self.skippable:
            try:
                self.output_artifacts = self.fill_output_artifacts(sysname, out_pdb=out_pdb, out_box=out_box)
                self.node_logger.info(f"Skipped {self.id} WorkNode.")
                return True
            except (FileNotFoundError, ValueError) as e:
                self.node_logger.debug(f"Can't skip {self.id} Got: {e}")
            except NotImplementedError:
                self.node_logger.debug(
                    f"Can't skip {self.id}. {self.__class__.__name__} did not implement `fill_output_artifacts()`"
                )
        return False

    # noinspection PyMethodMayBeStatic
    def fill_output_artifacts(
        self,
        sysname: str,
        *,
        out_pdb: filepath_t,
        out_box: BasePeriodicBox,
    ) -> ArtifactContainer:
        return ArtifactContainer(
            sysname,
            [
                ArtifactRegistry.create_instance_by_filename(
                    out_pdb, tags=self.tags[self.artifact_map["BaseBinderLigandStructureFile"]]
                ),
                out_box,
            ],
        )
