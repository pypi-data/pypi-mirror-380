import argparse
import inspect
from amberflow import flows
from amberflow.flows import BaseFlow


def get_opts(flow_choices):
    parser = argparse.ArgumentParser(description="Print a predefined AmberFlow Flow to stdout.")
    parser.add_argument(
        "flow_name",
        type=str,
        default=None,
        choices=flow_choices,
        help="The name of the Flow class to print",
    )
    args = parser.parse_args()
    return args.flow_name


def printflow():
    """
    Finds all available Flow classes. If a flow name is provided as an
    argument, it prints the source code of the entire file containing that flow.
    If no argument is provided, it lists all available flows.
    """
    # Discover all classes in the 'flows' module that are subclasses of BaseFlow
    flow_classes = {}
    for name, obj in inspect.getmembers(flows, inspect.isclass):
        if issubclass(obj, BaseFlow) and obj is not BaseFlow:
            flow_classes[name] = obj

    if not flow_classes:
        print("No Flow classes found in the amberflow.flows module.")
        return

    flow_name = get_opts(list(flow_classes.keys()))
    selected_flow_class = flow_classes[flow_name]

    # Get the source code of the entire file containing the selected flow class
    try:
        # Get the path of the file where the class is defined
        file_path = inspect.getsourcefile(selected_flow_class)
        if file_path is None:
            raise TypeError(f"Could not determine the source file for {flow_name}")

        with open(file_path, "r") as f:
            source_code = f.read()
        print(source_code)
    except (TypeError, FileNotFoundError) as e:
        print(f"\nError: Could not get source for '{flow_name}'.")
        print(f"Original error: {e}")


if __name__ == "__main__":
    printflow()
