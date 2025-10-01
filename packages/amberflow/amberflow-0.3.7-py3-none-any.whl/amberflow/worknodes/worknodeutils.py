from collections import deque
from logging import Logger
import warnings
from pathlib import Path
from string import Template
from typing import Optional, Union, Any
import mmap


import MDAnalysis as mda
import networkx as nx

from amberflow.artifacts import (
    BaseArtifact,
)
from amberflow.primitives import filepath_t, find_word_and_get_line

__all__ = [
    "TleapMixin",
    "AntechamberMixin",
    "runiverse",
    "wuniverse",
    "check_leap_log",
    "check_cpp_log",
    "get_periodic_box_parameters_pdb",
    "get_periodic_box_parameters_rst7",
    "get_molgraph",
    "draw_flow_graph",
]


class TleapMixin:
    resources: Optional[dict] = None
    leaprc: str = "leaprc"
    load_nonstandard: str = "load_nonstandard"
    load_pdb: str = "load_pdb"
    neutralize_ions: str = "neutralize_ions"
    save_amberparm: str = "save_amberparm"
    quit: str = "quit"

    supports = {
        "water": ("opc", "tip3p", "tip4pew", "spce"),
        "force_field": ("14SB", "19SB"),
        "atom_type": ("gaff", "gaff2"),
        "boxshape": ("orthorhombic", "truncated_octahedron"),
    }

    SOLVENT_TO_BOX = {
        "tip3p": "TIP3PBOX",
        "opc": "OPCBOX",
        "tip4pew": "TIP4PEWBOX",
        "spce": "SPCEBOX",
    }

    def check_supported(self, element: str, opt_type: str) -> None:
        try:
            supported_options = self.supports[opt_type]
            if element not in supported_options:
                err_msg = f"Unknown: {element}. Must be one of: {supported_options}"
                raise ValueError(err_msg)
        except KeyError:
            err_msg = f"Unknown option: {opt_type}. Must be one of: {list(self.supports.keys())}"
            raise ValueError(err_msg)

    def load_file(self, template_id: str, mapping: Optional[dict] = None) -> str:
        try:
            tleap_template_txt = Template(self.resources[template_id])
        except KeyError:
            err_msg = f"Invalid template {template_id}. Must be one of {self.resources.keys()}"
            raise ValueError(err_msg)

        return tleap_template_txt.substitute(mapping)

    def load_template(self, template_id: str) -> Template:
        try:
            tleap_template_txt = Template(self.resources[template_id])
        except KeyError:
            err_msg = f"Invalid template {template_id}. Must be one of {self.resources.keys()}"
            raise ValueError(err_msg)

        return tleap_template_txt


class AntechamberMixin:
    supports = {
        "atom_type": ("gaff", "gaff2", "abcg2", "bcc"),
        "charge_model": ("bcc", "abcg2"),
    }

    def check_supported(self, element: str, opt_type: str) -> None:
        try:
            supported_options = self.supports[opt_type]
            if element not in supported_options:
                err_msg = f"Unknown: {element}. Must be one of: {supported_options}"
                raise ValueError(err_msg)
        except KeyError:
            err_msg = f"Unknown option: {opt_type}. Must be one of: {list(self.supports.keys())}"
            raise ValueError(err_msg)


def check_leap_log(leap_log: filepath_t, node_logger: Logger, debug_warn: bool = False) -> None:
    if lines := find_word_and_get_line(leap_log, "Error!"):
        err_msg = f"Error! found in {leap_log}\n{lines}"
        node_logger.error(err_msg)
        raise RuntimeError(err_msg)
    if debug_warn:
        if lines := find_word_and_get_line(leap_log, "Warning!"):
            node_logger.warning(f"Warning! found in {leap_log}\n{lines}")


def check_cpp_log(leap_log: filepath_t, node_logger: Logger, debug_warn: bool = False) -> None:
    if lines := find_word_and_get_line(leap_log, "Error!"):
        err_msg = f"Error! found in {leap_log}\n{lines}"
        node_logger.error(err_msg)
        raise RuntimeError(err_msg)
    if debug_warn:
        if lines := find_word_and_get_line(leap_log, "Warning!"):
            node_logger.warning(f"Warning! found in {leap_log}\n{lines}")


def runiverse(infile: Union[filepath_t, BaseArtifact], to_guess: Optional[tuple] = None, **kwargs) -> mda.Universe:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        if to_guess is None:
            return mda.Universe(Path(infile), **kwargs)
        else:
            return mda.Universe(Path(infile), to_guess=to_guess)


def wuniverse(u: mda.Universe, outfile: filepath_t) -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        u.atoms.write(Path(outfile))


def get_periodic_box_parameters_pdb(boxed_pdb: filepath_t, margin: float = 0.0004) -> list[float]:
    """
    Reads the periodic box parameters from the first line of a PDB file.

    Args:
        boxed_pdb: The path to the rst7 file.
        margin: A small margin to add to the box dimensions to avoid precision issues, since CRYST1 records are not
        as precise as rst7 files.
    Returns:
        A list of six floats representing the box dimensions and angles.

    Raises:
        ValueError: If the file cannot be read, the last line is malformed,
                    or it does not contain enough values.
    """
    with open(boxed_pdb, "rb") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            # Find the end of the first line
            line_end = mm.find(b"\n")
            first_line = mm[:line_end].decode()

            if not first_line.startswith("CRYST1"):
                raise ValueError(f"{boxed_pdb} irst line ({first_line}) is not a CRYST1 record")

            try:
                # Split the line and slice the 6 numbers corresponding to the box dimensions
                parts = first_line.split()
                if len(parts) < 7:
                    raise ValueError("CRYST1 line is malformed or has too few values.")

                # Convert the relevant parts to floats
                box = [float(x) for x in parts[1:7]]
                box[0] = box[0] + margin
                box[1] = box[1] + margin
                box[2] = box[2] + margin
                return box

            except (ValueError, IndexError) as e:
                raise ValueError(f"Failed to parse CRYST1 line: {first_line}") from e


def get_periodic_box_parameters_rst7(boxed_rst7: filepath_t) -> list[float]:
    """
    Reads the periodic box parameters from the last line of an AMBER rst7 file.

    Args:
        boxed_rst7: The path to the PDB file.

    Returns:
        A list of six floats representing the box dimensions and angles.

    Raises:
        ValueError: If the file cannot be read, the last line is malformed, or it does not contain enough values.
    """
    try:
        with open(boxed_rst7, "rb") as f:
            # Seek to a position near the end of the file to read a chunk.
            # 1024 bytes is enough for typical box info lines.
            f.seek(0, 2)  # Go to the end of the file
            file_size = f.tell()
            f.seek(max(file_size - 1024, 0), 0)  # Go back 1024 bytes, or to the start

            # Read the final lines and get the last non-empty one
            lines = f.readlines()
            if not lines:
                raise ValueError("File is empty or could not be read.")

            last_line = lines[-1].decode().strip()

            # Parse the line
            parts = last_line.split()
            if len(parts) < 6:
                raise ValueError(f"Last line contains fewer than 6 values: '{last_line}'")

            # The first six values on the last line are the box parameters
            return [float(x) for x in parts[:6]]
    except (IOError, IndexError, ValueError) as e:
        raise ValueError(f"Failed to read or parse periodic box from {boxed_rst7}") from e


def get_molgraph(
    in_atoms: mda.core.groups.AtomGroup,
    start_atom: Optional[mda.core.groups.Atom] = None,
    logger: Optional[Logger] = None,
) -> nx.Graph:
    """
    build a graph out of an atom selection with bonds

    If a `start_atom` is provided, the graph is built by traversing bonds
    starting from that atom, capturing a single connected molecule. If
    `start_atom` is None, graphs for all atoms and bonds in the universe are built,
    which may result in a disconnected graph if multiple molecules are present.

    Args:
        in_atoms: An MDAnalysis AtomGroup containing atoms with bond information.
        start_atom (Optional): The MDAnalysis.Atom to start traversal from.
                               If None, all atoms in the universe are used.
        logger (Optional): If None, errors are raised without logging.

    Returns:
        A NetworkX.Graph representing the molecule's covalent structure.
    """
    if not hasattr(in_atoms, "bonds") or len(in_atoms.bonds) == 0:
        err_msg = "The MDAnalysis Universe does not contain bond information. "
        if logger:
            logger.error(err_msg)
        raise ValueError(err_msg)

    molgraph = nx.Graph()
    atom_indices = {at.index for at in in_atoms}
    if start_atom is None:
        for atom in in_atoms:
            attributes: dict[str, Any] = {
                "atomname": atom.name,
                "index": atom.index,
                "element": getattr(atom, "element", "X"),
                "resname": atom.resname,
                "resid": atom.resid,
            }
            molgraph.add_node(atom.index, **attributes)

        for bond in in_atoms.bonds:
            atom1_idx, atom2_idx = bond.in_atoms.indices
            molgraph.add_edge(atom1_idx, atom2_idx)
    else:
        if start_atom not in in_atoms:
            raise ValueError("The provided start_atom is not part of the universe selection.")

        queue = deque([start_atom])
        visited = {start_atom.index}

        # Add the starting node
        attributes: dict[str, Any] = {
            "atomname": start_atom.name,
            "index": start_atom.index,
            "element": getattr(start_atom, "element", "X"),
            "resname": start_atom.resname,
            "resid": start_atom.resid,
        }
        molgraph.add_node(start_atom.index, **attributes)

        while queue:
            current_atom = queue.popleft()
            for some_bond in current_atom.bonds:
                for neighbor in some_bond:
                    # Ensure the neighbor is part of the universe we are considering
                    if neighbor.index in atom_indices and neighbor.index not in visited:
                        visited.add(neighbor.index)
                        queue.append(neighbor)

                        neighbor_attributes: dict[str, Any] = {
                            "atomname": neighbor.name,
                            "index": neighbor.index,
                            "element": getattr(neighbor, "element", "X"),
                            "resname": neighbor.resname,
                            "resid": neighbor.resid,
                        }
                        molgraph.add_node(neighbor.index, **neighbor_attributes)
                        molgraph.add_edge(current_atom.index, neighbor.index)

    return molgraph


def draw_flow_graph(
    flow_graph,
    *,
    output_filename: Optional[str] = None,
    figsize: tuple[int, int] = (18, 18),
    node_size: int = 700,
    logger: Optional[Logger] = None,
) -> None:
    try:
        import matplotlib.pyplot as plt
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError(
            "Plotting dependencies are not installed. Please install them with:\n\n"
            "pip install matplotlib networkx pydot\n\n"
            "You also need to install Graphviz. See: https://graphviz.org/download/"
        )
    """
    Generates and saves a visualization of the pipeline's workflow graph.

    This function uses Graphviz (via pydot) to create a hierarchical 'dot' layout
    of the directed acyclic graph (DAG) and saves it to an image file.

    Args:
        pipeline: The pipeline instance to visualize.
        output_filename: The name of the output image file to save.
    """

    if not flow_graph.nodes:
        if logger is not None:
            logger.warning("Pipeline flow is empty. Nothing to draw.")
        return

    try:
        # Use graphviz for a top-to-bottom hierarchical layout
        pos = graphviz_layout(flow_graph, prog="dot")
    except OSError as e:
        if logger is not None:
            logger.error(
                "Graphviz layout failed. Please ensure Graphviz is installed and "
                "its 'bin' directory is in your system's PATH.\n"
                "Download from: https://graphviz.org/download/\n"
                f"Original error: {e}"
            )
        return

    plt.figure(figsize=figsize)

    # Use the node's `id` attribute for a clear and unique label
    node_labels = {node: node.id for node in flow_graph.nodes}

    # Draw the nodes
    nx.draw_networkx_nodes(flow_graph, pos, node_size=node_size, node_color="skyblue", alpha=0.9)

    # Draw the edges with arrows
    nx.draw_networkx_edges(
        flow_graph,
        pos,
        width=1.5,
        alpha=0.6,
        edge_color="gray",
        arrows=True,
        arrowstyle="-|>",
        arrowsize=25,
    )

    # Draw the node labels
    nx.draw_networkx_labels(flow_graph, pos, labels=node_labels, font_size=10, font_weight="bold")

    plt.title(f"Flow: {flow_graph.name}", fontsize=20)
    plt.axis("off")
    plt.tight_layout()
    if output_filename is not None:
        plt.savefig(output_filename, bbox_inches="tight", pad_inches=0.1, transparent=True)
        if logger is not None:
            logger.info(f"Pipeline graph saved to '{output_filename}'")
    plt.show()
