import contextlib
import mmap
import os
import shutil
import string
import sys
from io import StringIO
from logging import Logger
from pathlib import Path
import subprocess as sp
from typing import Final, Iterable, Optional

import parmed
from rdkit import Chem
from rdkit.Chem import rdFMCS


from amberflow.primitives import filepath_t, FileHandle, dirpath_t

__all__ = [
    "conv_build_resnames_set",
    "get_ngpus",
    "get_dir_size",
    "amb_to_pdb",
    "capture_stdout",
    "_run_command",
    "patch_pdb_with_lib",
    "patch_pdb_lib",
    "concatenate_pdbs",
    "assign_chain_ids",
    "remove_residues_pdb",
]


def conv_build_resnames_set(value):
    if isinstance(value, str):
        return {value}
    elif isinstance(value, Iterable):
        return set(value)
    else:
        return set()


def get_ngpus():
    try:
        p = sp.run(
            "nvidia-smi -L | wc -l",
            stdout=sp.PIPE,
            stderr=sp.PIPE,
            shell=True,
            text=True,
        )
        ngpus = int(p.stdout)
        assert ngpus != 0
    except (ValueError, AssertionError, Exception):
        raise RuntimeError("No GPUs detected. Can't run locuaz.")
    return ngpus


def get_dir_size(folder: Path) -> float:
    # noinspection PyPep8Naming
    B_TO_MB: Final = 1048576
    total_size = 0
    for path, _, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)  # type: ignore
    return total_size / B_TO_MB


def amb_to_pdb(top_filepath: filepath_t, rst_filepath: filepath_t) -> FileHandle:
    """
    Convert AMBER topology and restart files to PDB format.

    Parameters
    ----------
    top_filepath : Path
        The path to the AMBER topology file.
    rst_filepath : Path
        The path to the AMBER restart file.

    Returns
    -------
    FileHandle
        A `FileHandle` object pointing to the generated PDB file.
    """
    amb = parmed.load_file(str(top_filepath), str(rst_filepath))
    pdb_path = top_filepath.with_suffix(".pdb")
    amb.save(str(pdb_path))  # type: ignore
    return FileHandle(pdb_path)


@contextlib.contextmanager
def capture_stdout(new_stdout: Optional[StringIO] = None):
    """
    A context manager to temporarily suppress stdout.

    Args:
        new_stdout: An optional StringIO object to capture the output.
                    If None, output is discarded.

    Yields:
        The StringIO object that captured the output.
    """
    # If no buffer is provided, create a dummy one to discard output
    if new_stdout is None:
        new_stdout = StringIO()

    # Save the original stdout so we can restore it later
    original_stdout = sys.stdout

    # Redirect stdout to the new buffer
    sys.stdout = new_stdout
    try:
        # Yield control back to the 'with' block
        yield new_stdout
    finally:
        # Always restore the original stdout, even if errors occur
        sys.stdout = original_stdout


def _run_command(
    command: str,
    logger: Logger,
    *,
    cwd: Optional[dirpath_t] = None,
    env: Optional[dict] = None,
    check: bool = True,
    timeout: Optional[int] = None,
) -> sp.CompletedProcess:
    try:
        p = sp.run(
            command,
            stdout=sp.PIPE,
            stderr=sp.PIPE,
            text=True,
            cwd=str(cwd) if cwd is not None else None,
            env=env,
            check=check,
            shell=True,
            timeout=timeout,
        )
        if p.stdout:
            logger.debug(f"STDOUT: {p.stdout}")
        if p.stderr:
            logger.debug(f"STDERR: {p.stderr}")
        return p
    except sp.TimeoutExpired as e:
        err_msg = f"Command timed out after {timeout} seconds: {command}"
        logger.error(err_msg)
        raise RuntimeError(err_msg) from e
    except sp.CalledProcessError as e:
        err_msg = f"Command failed with exit code {e.returncode}: {command}"
        logger.error(err_msg)
        logger.error(f"STDOUT:\n{e.stdout}")
        logger.error(f"STDERR:\n{e.stderr}")
        raise RuntimeError(err_msg) from e
    except Exception as e:
        err_msg = f"Unknown error running command {e}"
        logger.error(err_msg)
        raise RuntimeError(err_msg)


# noinspection PyTypeChecker, PyUnresolvedReferences
def patch_pdb_with_lib(tgt_mol: filepath_t, ref_mol: filepath_t, *, logger: Optional[Logger] = None):
    mcs_result = rdFMCS.FindMCS([ref_mol, tgt_mol], timeout=10)
    matches_mol1 = ref_mol.GetSubstructMatches(mcs_result.queryMol)
    matches_mol2 = tgt_mol.GetSubstructMatches(mcs_result.queryMol)
    match1 = set(idx for match in matches_mol1 for idx in match)
    match2 = set(idx for match in matches_mol2 for idx in match)

    atom_map_1_to_2 = dict(zip(match1, match2))
    atom_map_2_to_1 = {v: k for k, v in atom_map_1_to_2.items()}
    # Create an editable version of tgt_mol
    editable_tgt_mol = Chem.RWMol(tgt_mol)

    # Get full sets of atom indices for identifying differences
    all_indices_tgt_mol = set(range(tgt_mol.GetNumAtoms()))
    mcs_indices_tgt_mol = set(atom_map_1_to_2.keys())
    diff_indices_tgt_mol = all_indices_tgt_mol - mcs_indices_tgt_mol

    # A) Transfer properties for atoms IN the MCS
    for idx1, idx2 in atom_map_1_to_2.items():
        atom1 = editable_tgt_mol.GetAtomWithIdx(idx1)
        atom2 = ref_mol.GetAtomWithIdx(idx2)

        atom1.SetAtomicNum(atom2.GetAtomicNum())
        atom1.GetPDBResidueInfo().SetName(atom2.GetPDBResidueInfo().GetName())

    # B) Transfer properties for atoms NOT in the MCS
    for idx1 in diff_indices_tgt_mol:
        atom1_orig = tgt_mol.GetAtomWithIdx(idx1)
        # Find its neighbor that is in the MCS (the "anchor")
        for neighbor in atom1_orig.GetNeighbors():
            if neighbor.GetIdx() in mcs_indices_tgt_mol:
                anchor_idx1 = neighbor.GetIdx()
                break
        else:
            continue  # Should not happen in a connected molecule

        # Find the corresponding anchor atom in ref_mol
        anchor_idx2 = atom_map_1_to_2[anchor_idx1]
        anchor_atom2 = ref_mol.GetAtomWithIdx(anchor_idx2)

        # Find the neighbor of the anchor in ref_mol that is NOT in the MCS
        for neighbor2 in anchor_atom2.GetNeighbors():
            if neighbor2.GetIdx() not in atom_map_2_to_1:
                target_atom2 = neighbor2
                break
        else:
            continue  # Should not happen

        # Now, mutate the differing atom in our editable tgt_mol
        atom_to_change = editable_tgt_mol.GetAtomWithIdx(idx1)
        if logger is not None:
            logger.info(
                f"Changing Atom {atom_to_change.GetPDBResidueInfo().GetName().strip()} "
                f"-> {target_atom2.GetPDBResidueInfo().GetName().strip()}"
            )

        atom_to_change.SetAtomicNum(target_atom2.GetAtomicNum())
        atom_to_change.GetPDBResidueInfo().SetName(target_atom2.GetPDBResidueInfo().GetName())

    final_mol = editable_tgt_mol.GetMol()
    return final_mol


# noinspection PyTypeChecker, PyUnresolvedReferences
def patch_pdb_lib(
    in_pdb: filepath_t, in_lib: filepath_t, out_pdb: filepath_t, out_lib: filepath_t, *, logger: Optional[Logger] = None
) -> None:
    lib_obj = parmed.load_file(str(in_lib))
    pdb_obj = parmed.load_file(str(in_pdb))

    if len(lib_obj) != 1 and len(pdb_obj.residues) != 1:
        err_msg = (
            f"{in_pdb} has {len(pdb_obj.residues)} residues and {in_lib} has {len(lib_obj)} residues. "
            "Both must have exactly one residue."
        )
        if logger:
            logger.error(err_msg)
        raise ValueError(err_msg)

    # First, fix the PDB
    ref_template_struct = next(iter(lib_obj.values()))
    ref_mol = ref_template_struct.to_structure().rdkit_mol
    pdb_mol = pdb_obj.rdkit_mol
    fixed_pdbmol = patch_pdb_with_lib(pdb_mol, ref_mol, logger=logger)
    Chem.MolToPDBFile(fixed_pdbmol, out_pdb)

    # Now, assign the coordinates from the PDB to the lib file
    fixed_pdb_obj = parmed.load_file(str(out_pdb))
    pdb_atoms = {atom.name: atom for atom in fixed_pdb_obj.atoms}
    num_matched = 0
    for template_atom in ref_template_struct.atoms:
        if template_atom.name in pdb_atoms:
            source_atom = pdb_atoms[template_atom.name]
            template_atom.xx = source_atom.xx
            template_atom.xy = source_atom.xy
            template_atom.xz = source_atom.xz
            num_matched += 1
        else:
            err_msg = f"Atom '{template_atom.name}' in OFF file not found in source coordinates."
            if logger:
                logger.error(err_msg)
            raise ValueError(err_msg)
    if num_matched != len(ref_template_struct.atoms):
        err_msg = f"Could not map all atoms between structures. Matched {num_matched} out of {len(ref_template_struct.atoms)}."
        if logger:
            logger.error(err_msg)
        raise ValueError(err_msg)

    parmed.amber.offlib.AmberOFFLibrary.write(lib_obj, str(out_lib))


def concatenate_pdbs(pdb_files: list[Path], output_path: Path) -> None:
    """
    Concatenates multiple PDB files into a single file

    This function reads each PDB file, removes leading `HEADER_RECORDS` and trailing 'END' records,
    ensures a 'TER' record exists at the end of each segment, and writes the sanitized content to an output file.
    A single 'END' record is added to the very end of the final concatenated file.

    Args:
        pdb_files: A list of Path objects for the input PDB files.
        output_path: The Path object for the output file.
    Raises:
        ValueError: If no atomic data is found in any of the input PDB files.
    """
    # noinspection PyPep8Naming
    HEADER_RECORDS = {b"HEADER", b"TITLE", b"CRYST1", b"REMARK"}
    with open(output_path, "wb") as f_out:
        for pdb_file in pdb_files:
            with open(pdb_file, "rb") as f_in:
                with mmap.mmap(f_in.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    # Slurp the file
                    lines = mm.read().splitlines()

                    # Find the start of the atomic data
                    for i, line in enumerate(lines):
                        if len(line) >= 6 and line[:6].strip().upper() in HEADER_RECORDS:
                            continue
                        else:
                            start_index = i
                            break
                    else:
                        raise ValueError(f"No atomic data found in {pdb_file}")

                    # Process lines from the first non-header line onwards.
                    atom_lines = lines[start_index:]

                    # Filter out empty lines, so it doesn't break the next step
                    content_lines = [line for line in atom_lines if line.strip()]
                    # Remove all trailing END records.
                    while content_lines and content_lines[-1].strip().upper() == b"END":
                        content_lines.pop()

                    has_ter = False
                    if content_lines and content_lines[-1].strip().upper() == b"TER":
                        has_ter = True
                    # Write the sanitized lines for the current PDB.
                    for line in content_lines:
                        f_out.write(line + b"\n")
                    # If there was no TER record, add one.
                    if not has_ter:
                        f_out.write(b"TER\n")

        # After processing all files, add a single END record.
        f_out.write(b"END\n")


def assign_chain_ids(input_pdb_path: filepath_t, output_pdb_path: filepath_t) -> None:
    """
    Assigns a unique chain ID to each molecule in a PDB file using mmap.

    This function processes a PDB file, identifying molecules separated by
    "TER" records. It assigns a chain ID character from A-Z, then a-z, to
    each molecule. The modification is done in-place on a copy of the
    original file using a memory map for high performance.

    If more than 52 molecules are present, subsequent molecules will not
    have their chain ID modified.

    Args:
        input_pdb_path (filepath_t): The path to the source PDB file.
        output_pdb_path (filepath_t): The path where the modified PDB file
    """
    # Create a generator for the chain IDs (A-Z, then a-z)
    chain_id_chars = iter(string.ascii_uppercase + string.ascii_lowercase)

    # mmap works directly on the output file
    try:
        shutil.copy(input_pdb_path, output_pdb_path)
    except shutil.SameFileError:
        pass
    with open(output_pdb_path, "r+b") as f:
        # Create a memory-mapped file object
        with mmap.mmap(f.fileno(), 0) as mm:
            # Get the first chain ID for the first molecule
            current_chain_id = next(chain_id_chars, None)

            line_start = 0
            while line_start < len(mm):
                # Find the end of the current line
                line_end = mm.find(b"\n", line_start)
                if line_end == -1:  # End of file
                    line_end = len(mm)

                # Check ATOM/HETATM records
                # The chain ID is at a fixed position (column 22, index 21)
                if mm[line_start : line_start + 6] in (b"ATOM  ", b"HETATM"):
                    if current_chain_id is not None:
                        # Modify the byte in-place
                        mm[line_start + 21] = ord(current_chain_id)

                # Check for molecule separator
                elif mm[line_start : line_start + 3] == b"TER":
                    # Move to the next chain ID for the next molecule
                    current_chain_id = next(chain_id_chars, None)

                # Move to the start of the next line
                line_start = line_end + 1


def remove_residues_pdb(input_pdb_path: filepath_t, output_pdb_path: filepath_t, resnames: tuple[str]) -> None:
    """
    Removes ATOM/HETATM that match the atom names in a PDB file using mmap.

    Args:
        input_pdb_path (filepath_t): The path to the source PDB file.
        output_pdb_path (filepath_t): The path where the modified PDB file
        resnames (tuple[str]): A tuple of residue names to remove.
    """
    if len(resnames) == 0:
        raise ValueError("atom_names must be a non-empty tuple")
    set_resnames_bytes = {s.rjust(3).encode("ascii") for s in resnames}

    # mmap works directly on the output file
    if input_pdb_path == output_pdb_path:
        backup_pdb_path = Path(input_pdb_path).with_stem("backup_remove_atom_name")
        shutil.copy(input_pdb_path, backup_pdb_path)
        input_pdb_path = backup_pdb_path

    with open(input_pdb_path, "rb") as f_in, open(output_pdb_path, "wb") as f_out:
        with mmap.mmap(f_in.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            for line in iter(mm.readline, b""):
                keep_line = True
                # Only perform checks on ATOM/HETATM records
                if line.startswith((b"ATOM  ", b"HETATM")):
                    # PDB residue name is in columns 18-20 (slice 17:20)
                    if line[17:20] in set_resnames_bytes:
                        # If the residue name is in our set, flag the line for removal
                        keep_line = False
                if keep_line:
                    f_out.write(line)
