# Practical 12 - Common algorithms
# tarvk002
#


# Step 1
def depth_first(tree, node):
    """Traverse the tree from node in depth-first order."""
    print(tree[node]["data"])
    for child in tree[node]["children"]:
        depth_first(tree,child)
    pass


def breadth_first(tree, root_node):
    """Traverse the tree from root_node in breadth-first order."""
    queue = [root_node]
    while queue:
        current = queue.pop(0)
        print(tree[current]["data"])
        queue.extend(tree[current]["children"])
    pass


def main():
    numbers = [53, 22, 79, 17, 83, 11, 40, 36]

    # A tree with node 1 as the root node.
    tree = {
        1: {"data": "Apple", "children": [2, 3, 4]},
        2: {"data": "Banana", "children": [5, 6]},
        3: {"data": "Cherry", "children": [7]},
        4: {"data": "Grape", "children": []},
        5: {"data": "Melon", "children": []},
        6: {"data": "Orange", "children": []},
        7: {"data": "Pear", "children": []},
    }

    print("=== Depth First Traverse ===")
    depth_first(tree, 1)
    print()

    print("=== Breadth First Traverse ===")
    breadth_first(tree, 1)


main()
