import json

def resolve(pkg, deps, memo=None):
    """
    Recursive function that digs into the provided deps dictionary and
    constructs the full dependency graph to return.

    :param pkg: str
        - String representing the current package that is being resolved
    :param deps: dict
        - Dictionary of all dependencies, to use for parsing
    :param memo: dict
        - Dictionary storing current memory of dependencies
    :return: resolved_deps: dict
        - Dictionary containing full dependency graph.
    """

    # Set memo to empty dict is None, to avoid mutable as default
    memo = {} if memo is None else memo

    # If the package's dependencies have been resolved before, return them.
    if pkg in memo:
        return memo[pkg]

    # If package has no dependencies, it's a leaf!
    if not deps.get(pkg):
        return {}

    # Resolve dependencies for the package.
    resolved_deps = {}
    for dep in deps[pkg]:
        resolved_deps[dep] = resolve(dep, deps, memo)

    # Store found dependencies for package to not need to traverse next time
    memo[pkg] = resolved_deps

    return resolved_deps


def get_full_dependency_graph(filename):
    """
    Main function that loads data and calls resolve function with proper arguments
    to find full dependency graph.

    :param filename: str
        - String containing path to filename
    :return: _ : dict
        - Dictionary containing full dependency graph
    """
    with open(filename, 'r') as f:
        data = json.load(f)

    return {pkg: resolve(pkg, data) for pkg in data}


def print_graph(graph, indent=0):
    """
    A simple function that prints out the full dependency graph in a more pleasing manner.

    :param graph: dict
        - Dictrionary containing full dependency graph
    :param indent: int
        - Offers adjustment on indent level
    :return: None
    """
    for pkg, deps in graph.items():
        print('  ' * indent + '- ' + pkg)
        print_graph(deps, indent + 1)

