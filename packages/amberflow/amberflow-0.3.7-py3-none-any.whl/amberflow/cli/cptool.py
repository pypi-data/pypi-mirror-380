import argparse
import pickle
import shutil
from pathlib import Path
from typing import Optional, Collection, Any, List, Dict

import networkx as nx

from amberflow.pipeline import change_cwd
from amberflow.primitives import dirpath_t
from amberflow.worknodes import WorkNodeStatus

try:
    import amberflow  # noqa: F401
except ModuleNotFoundError:
    raise ModuleNotFoundError("Install amberflow: pip install amberflow")
except Exception as ee:
    raise ModuleNotFoundError("Unknown error when trying to import amberflow") from ee


# ANSI colors
class Colors:
    """A collection of ANSI escape codes for styling terminal output."""

    # Standard Foreground Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright Foreground Colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background Colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Styles
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    # Combined for convenience
    MAGENTA_ON_WHITE = "\033[95;107m"
    WHITE_ON_BLACK = "\033[97;40m"
    BLACK_ON_WHITE = "\033[30;107m"

    @staticmethod
    def get_cycle() -> List[str]:
        """
        Dynamically provides a list of distinct, readable color attributes
        from the class for cycling through in the terminal output. It prioritizes
        bright colors for visibility.
        """
        colors = []
        for name, value in Colors.__dict__.items():
            # Introspect the class to find attributes that are uppercase (our convention for colors)
            # and are strings (the ANSI codes). We select BRIGHT colors for readability.
            if name.isupper() and name.startswith("BRIGHT_") and "BLACK" not in name and isinstance(value, str):
                colors.append(value)

        # Provide a sensible default if the introspection somehow fails.
        return colors if colors else ["\033[96m", "\033[92m", "\033[93m", "\033[95m", "\033[94m", "\033[97m"]


def clean_worknode_dirs(
    root_path: dirpath_t,
    systems: Dict[str, dirpath_t],
    pending_nodes_dirnames: dict[str, str],
    exclude_systems: Optional[List[str]] = None,
):
    """
    Deletes worknode directories within each system folder, based on data from a checkpoint.

    Args:
        root_path (Path): The root working directory of the pipeline ('cwd' from checkpoint).
        systems (Dict[str, Path]): A map of system names to their paths.
        pending_nodes_dirnames (list[str]): A list of worknode IDs to remove.
        exclude_systems (Optional[List[str]]): A list of system names to exclude.
    """
    print(f"{Colors.YELLOW}--- Starting Hard Cleanup ---{Colors.RESET}")
    root_path = Path(root_path)
    if not root_path.is_dir():
        print(f"{Colors.RED}Error: Root directory '{root_path}' from checkpoint not found.{Colors.RESET}")
        return
    dirs_to_delete: List[Path] = []
    exclude_systems_set = set(exclude_systems) if exclude_systems else set()

    # First, gather a list of all directories that are candidates for deletion.
    for system_name, sys_path in systems.items():
        if system_name in exclude_systems_set:
            print(f"   - SKIPPING system '{system_name}' (excluded).")
            continue
        system_path = Path(sys_path)
        if not system_path.is_dir():
            print(
                f"   - {Colors.YELLOW}WARNING: System directory not found at '{system_path}'. Skipping.{Colors.RESET}"
            )
            continue

        # Check which pending node directories actually exist in this system
        for node_dirname in pending_nodes_dirnames.values():
            wn_dirpath = system_path / node_dirname
            if wn_dirpath.is_dir():
                dirs_to_delete.append(wn_dirpath)
    if not dirs_to_delete:
        print(f"{Colors.GREEN}   - No matching directories found to delete.{Colors.RESET}")
        print(f"{Colors.YELLOW}--- Hard Cleanup Finished ---\n{Colors.RESET}")
        return

    print(
        f"\n{Colors.BOLD}{Colors.YELLOW}The following {len(dirs_to_delete)} directories are scheduled for deletion:{Colors.RESET}"
    )
    for dir_path in dirs_to_delete:
        print(f"   - {dir_path}")

    try:
        prompt = f"\n{Colors.BOLD}{Colors.RED}Are you sure you want to permanently delete these directories? [y/N]: {Colors.RESET}"
        confirm = input(prompt).strip().lower()
    except KeyboardInterrupt:
        print(f"\n{Colors.CYAN}   - Deletion cancelled by user.{Colors.RESET}")
        print(f"{Colors.YELLOW}--- Hard Cleanup Finished ---\n{Colors.RESET}")
        return

    if confirm != "y":
        print(f"{Colors.CYAN}   - Deletion cancelled by user.{Colors.RESET}")
        print(f"{Colors.YELLOW}--- Hard Cleanup Finished ---\n{Colors.RESET}")
        return

    # Now, proceed with deleting the confirmed directories.
    print(f"{Colors.YELLOW}--- Deleting confirmed directories... ---{Colors.RESET}")
    for wn_dirpath in dirs_to_delete:
        try:
            print(f"   - {Colors.RED}DELETING: {wn_dirpath}{Colors.RESET}")
            shutil.rmtree(wn_dirpath)
        except OSError as e:
            print(f"   - {Colors.YELLOW}WARNING: Could not delete '{wn_dirpath}'. Error: {e}. Skipping.{Colors.RESET}")

    print(f"{Colors.YELLOW}--- Hard Cleanup Finished ---\n{Colors.RESET}")


def get_opts() -> tuple[list[Path], dict]:
    parser = argparse.ArgumentParser(
        description="Edit AmberFlow checkpoints by performing a topological sort of the flow",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("pickle_paths", nargs="+", type=Path, help="Paths to the checkpoint pickle files.")

    soft_group = parser.add_argument_group("Soft Cleanup (Modify Node Status)")
    soft_group.add_argument(
        "--but",
        type=str,
        metavar="ID",
        help="Mark all nodes as COMPLETED, with the exception of the input node, which will be marked as PENDING",
    )
    soft_group.add_argument(
        "--from",
        type=str,
        metavar="ID",
        help=(
            "Mark all nodes as COMPLETED, until the input node is found, then mark all nodes as PENDING, "
            "including the input node"
        ),
    )
    soft_group.add_argument(
        "--just", type=str, metavar="ID", help="Mark only the input node as PENDING, others remain unchanged"
    )
    soft_group.add_argument(
        "--source",
        type=str,
        help="Perform all operations using the input node as the source for the topological sort",
    )
    soft_group.add_argument(
        "--to",
        type=str,
        help=(
            "FORBIDDEN. WorkNodes depend on previous nodes output, re-running a node without running its descendants "
            "can have surprising results."
        ),
    )
    soft_group.add_argument(
        "--cwd",
        type=str,
        help="Change the root dir of the whole Pipeline (worknodes included)",
    )

    hard_group = parser.add_argument_group("Hard Cleanup (Delete Directories)")
    hard_group.add_argument(
        "--hard",
        action="store_true",
        help="WorkNodes marked as PENDING get their directories deleted",
    )
    hard_group.add_argument(
        "--exclude-systems",
        nargs="+",
        metavar="SYSTEM",
        help="Space-separated list of system names to exclude from the WorkNode directory deletion.",
    )
    parser.add_argument(
        "--nobackup",
        action="store_true",
        default=False,
        help="Disable backup creation for the original pickle file. Default: a backup is created, if an edit is made.",
    )

    args = parser.parse_args()
    opts = vars(args)

    exclusive_args = tuple(["but", "from", "just", "cwd"])
    if sum([1 for key in exclusive_args if opts.get(key)]) > 1:
        parser.error(f"Only one of the arguments {exclusive_args} can be used at a time.")

    if not opts.get("but") and not opts.get("from"):
        opts["print"] = True

    for path in args.pickle_paths:
        if not path.exists():
            parser.error(f"File not found: '{path}'")

    return args.pickle_paths, opts


def do_all_but(dag, node_id) -> dict[str, str]:
    """Sets all nodes to COMPLETED except the target node."""
    pending_nodes: dict[str, str] = {}
    for node in dag.nodes:
        if node.id == node_id:
            node.status = WorkNodeStatus.PENDING
            pending_nodes[node.id] = node.out_dirname
        else:
            node.status = WorkNodeStatus.COMPLETED
    return pending_nodes


def do_from(dag, node_id) -> dict[str, str]:
    """Sets nodes before the target to COMPLETED and from the target onwards to PENDING."""
    pending_nodes: dict[str, str] = {}
    start: bool = False
    # Use topological sort to respect dependencies
    for node in nx.topological_sort(dag):
        if start or node.id == node_id:
            node.status = WorkNodeStatus.PENDING
            pending_nodes[node.id] = node.out_dirname
            start = True
        else:
            node.status = WorkNodeStatus.COMPLETED
    return pending_nodes


def printout(dag, *, systems: Collection[str], cwd: dirpath_t, node_id: Optional[str] = None):
    """Prints the status of the workflow graph to the console."""
    print("\n\t\t\t Systems \n")
    print(" ".join(systems))
    print("\n\t\t\t Root directory \n")
    print(cwd)
    print("\n\t\t\t Nodes \n")
    status_list = []
    for node in nx.topological_sort(dag):
        status_name = node.status.name
        color_map = {
            "COMPLETED": Colors.GREEN,
            "PENDING": Colors.BLUE,
            "FAILED": Colors.RED,
        }
        color = color_map.get(status_name, "")
        colored_status = f"{color}{status_name:<10}{Colors.RESET}"
        status_list.append(f"{node.id:<40}: {colored_status}")

    nodes_per_line = 3
    for i in range(0, len(status_list), nodes_per_line):
        chunk = status_list[i : i + nodes_per_line]
        print(" | ".join(chunk))
    print()

    if node_id:
        target_node = next((n for n in dag.nodes if n.id == node_id), None)
        if target_node and (predecessors := list(dag.predecessors(target_node))):
            color_cycle = Colors.get_cycle()
            num_colors = len(color_cycle)

            colored_pred_ids = [
                f"{color_cycle[i % num_colors]}{p.id}{Colors.RESET}" for i, p in enumerate(predecessors)
            ]
            pred_ids_str = ", ".join(colored_pred_ids)

            print(f"\t\t\t{Colors.YELLOW}--- REMINDER ---{Colors.RESET}")
            print(f"    Predecessors for '{Colors.BOLD}{node_id}{Colors.RESET}' are: {pred_ids_str}")


def edit_cpt(cpt_path: Path, opts: dict[str, Any]):
    with open(cpt_path, "rb") as f:
        try:
            data = pickle.load(f)
        except (pickle.UnpicklingError, EOFError) as e:
            raise RuntimeError(f"Error unpickling data from {cpt_path}: {e}") from e

    if not isinstance(data, dict) or "flow" not in data or "systems" not in data or "cwd" not in data:
        raise ValueError(f"Checkpoint file '{cpt_path}' does not contain the required keys ('flow', 'systems', 'cwd').")

    cwd = data["cwd"]
    systems = data["systems"]
    artifacts = data["artifacts"]
    dag = data["flow"]

    if source_id := opts.get("source"):
        source_node = next((n for n in dag.nodes if n.id == source_id), None)
        if not source_node:
            raise ValueError(f"Could not find a node with ID '{source_id}' in the DAG.")
        subgraph = dag.subgraph(nx.descendants(dag, source_node) | {source_node})
    else:
        subgraph = dag

    pending_nodes: dict[str, str] = {}
    node_id = None
    edit_mode = True
    edit_cwd = False
    if opts.get("but"):
        node_id = opts["but"]
        print(f"Setting all nodes to COMPLETED except '{node_id}' which will be PENDING.")
        pending_nodes = do_all_but(subgraph, node_id)
    elif opts.get("from"):
        node_id = opts["from"]
        print(f"Setting nodes before '{node_id}' to COMPLETED, and from '{node_id}' onwards to PENDING.")
        pending_nodes = do_from(subgraph, node_id)
    elif new_cwd := opts.get("cwd"):
        cwd, systems, artifacts, dag = change_cwd(
            cwd=data["cwd"], new_cwd=Path(new_cwd), systems=systems, artifacts=artifacts, flow=dag
        )
        edit_cwd = True
    else:  # just print
        opts["nobackup"] = True
        edit_mode = False

    if edit_mode:
        if len(pending_nodes) == 0 and not edit_cwd:
            raise ValueError(f"Could not find a node with ID '{node_id}' in the DAG.")

    printout(subgraph, systems=systems.keys(), cwd=cwd, node_id=node_id)
    data["flow"] = dag
    data["cwd"] = cwd
    data["systems"] = systems
    data["artifacts"] = artifacts

    if opts["hard"]:
        clean_worknode_dirs(
            root_path=cwd,
            systems=systems,
            exclude_systems=opts.get("exclude_systems"),
            pending_nodes_dirnames=pending_nodes,
        )

    if not opts.get("nobackup", False):
        i = 0
        backup_path = cpt_path.with_stem(f"backup_pickle_{i}")
        # Give a unique name to the backup file
        while backup_path.exists():
            i += 1
            backup_path = cpt_path.with_stem(f"backup_pickle_{i}")
        shutil.copy(cpt_path, backup_path)
        print(f"Created a backup of the original file at '{backup_path}'.")

    if edit_mode:
        # Write away
        with open(cpt_path, "wb") as f:
            # noinspection PyTypeChecker
            pickle.dump(data, f)


def cptool():
    cpt_paths, opts = get_opts()
    for cpt in cpt_paths:
        print("\n\t\t\t", Colors.BLACK_ON_WHITE, f"Checkpoint: '{cpt}'", Colors.RESET, "\n")
        edit_cpt(cpt, opts)


if __name__ == "__main__":
    cptool()
