import argparse
import pickle
from pathlib import Path

import networkx as nx
from typing import Hashable

try:
    import amberflow  # noqa: F401
except ModuleNotFoundError:
    raise ModuleNotFoundError("Install amberflow: pip install amberflow")
except Exception as ee:
    raise ModuleNotFoundError("Unknown error when trying to import amberflow") from ee


def get_opts() -> Path:
    parser = argparse.ArgumentParser(description="Print an AmberFlow Flow from a pickled file.")
    parser.add_argument("pickle_path", type=Path, help="The path to the checkpoint or Pipeline pickle file.")

    args = parser.parse_args()
    pickle_path: Path = args.pickle_path

    if not pickle_path.exists():
        raise FileNotFoundError(f"Error: Could not find '{pickle_path}'.")

    return pickle_path


def _print_tree_recursive(
    graph: nx.DiGraph, node: Hashable, prefix: str, is_last: bool, printed_nodes: set[Hashable]
) -> None:
    connector = "└── " if is_last else "├── "

    # Check if the node has already been printed
    if node in printed_nodes:
        # If so, print a reference and stop this branch
        print(f"{prefix}{connector}{node} [...]")
        return

    # 1. Print the current node
    print(f"{prefix}{connector}{node}")
    printed_nodes.add(node)  # Mark node as printed

    # 2. Prepare the prefix for the children
    child_prefix = prefix + ("    " if is_last else "|   ")

    # 3. Recurse on children
    children = list(graph.successors(node))
    for i, child in enumerate(children):
        is_child_last = i == len(children) - 1
        _print_tree_recursive(graph, child, child_prefix, is_child_last, printed_nodes)


# noinspection PyUnreachableCode
def print_dag(graph: nx.DiGraph) -> None:
    """
    Prints a NetworkX Directed Acyclic Graph (DAG) as a single, unified tree.

    Args:
        graph: A `networkx.DiGraph` object that must be a DAG.

    Raises:
        TypeError: If the input is not a `networkx.DiGraph`.
        ValueError: If the input graph contains a cycle.
    """
    if not isinstance(graph, nx.DiGraph):
        raise TypeError("Input must be a networkx.DiGraph object.")

    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Input graph must be a Directed Acyclic Graph (DAG).")

    roots = sorted([node for node, in_degree in graph.in_degree() if in_degree == 0])
    if not roots:
        print("Graph has no root nodes to print.")
        return

    printed_nodes: set[Hashable] = set()

    for i, root in enumerate(roots):
        if root in printed_nodes:
            continue  # Skip root if it was reached as a child of another root
        if i > 0:
            print()
        print(root)
        printed_nodes.add(root)

        children = list(graph.successors(root))
        for j, child in enumerate(children):
            is_child_last = j == len(children) - 1
            _print_tree_recursive(graph, child, "", is_child_last, printed_nodes)


def printdag():
    """
    Prints the flow out of a checkpoint or Pipeline pickle file.
    """
    dag_path = get_opts()
    with open(dag_path, "rb") as f:
        try:
            some_obj = pickle.load(f)
        except pickle.UnpicklingError as e:
            raise RuntimeError(f"Error unpickling the pipeline from {dag_path}: {e}") from e
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred while unpickling the pipeline: {e}") from e
    if isinstance(some_obj, dict):
        if "flow" not in some_obj:
            raise ValueError(f"Checkpoint {dag_path} does not contain a 'flow' key.")
        dag = some_obj["flow"]
    else:
        if not hasattr(some_obj, "flow"):
            raise ValueError(f"Pipeline {dag_path} does not have a 'flow' attribute.")
        dag = some_obj.flow

    if dag is None:
        raise ValueError(f"Could not find a DAG in {dag_path}.")
    else:
        print_dag(dag)


if __name__ == "__main__":
    printdag()
