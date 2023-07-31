import os
import json
from .graph import get_full_dependency_graph

def test_dependency_graph():

    # Create a temporary JSON file for testing
    test_file = "tmp/test_deps.json"
    with open(test_file, "w") as f:
        json.dump({
            "pkg1": ["pkg2", "pkg3"],
            "pkg2": ["pkg3"],
            "pkg3": []
        }, f)

    # Expected resolved dependency graph
    expected = {
        "pkg1": {"pkg2": {"pkg3": {}}, "pkg3": {}},
        "pkg2": {"pkg3": {}},
        "pkg3": {}
    }

    # Run the function and compare with expected output
    assert get_full_dependency_graph(test_file) == expected

    try:
        os.remove(test_file)
    except FileNotFoundError:
        pass
