class Node:
    """
    Docstring
    """

    pass

# Binary Tree
# Create a Binary Tree class
# Define a method for each of the depth first traversals:
# pre order
# in order
# post order
# Each depth first traversal method should return an array of values, ordered appropriately.


class BinaryTree:
    """
    Docstring
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, values=[]):
        # root >> left >> right
        # tree.root = 4
        #                       4
        #                     /   \
        #                   7      18
        #                 /   \   /   \
        #                3     1 5     11

        # expected   [4, 7, 3, 1, 18, 5, 11]
        # walk_through [4, 7, 3, 1, 18, 5, 11]

        def walk(input_node, value_list):
            if not input_node:
                return
        # Do something with the root
            value_list.append(input_node.value)
        # Do something with root.left
            walk(input_node.left, value_list)
        # Do something with root.right1
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self):
        # left >> root >> right
        pass

    def post_order(self):
        # left >> right >> root
        pass


class BinarySearchTree(BinaryTree):
    """
    Docstring
    """

    def add():
        pass

    def contains():
        pass
