import os
from .graph import get_full_dependency_graph, print_graph

if __name__ == "__main__":
    try:
        # Get the directory of the current script
        dir_path = os.path.dirname(os.path.abspath(__file__))

        filename = "deps1.json"
        graph = get_full_dependency_graph(dir_path + "/tmp/" + filename)
        print_graph(graph)
    except Exception as e:
        print(f"Error: {e}")
