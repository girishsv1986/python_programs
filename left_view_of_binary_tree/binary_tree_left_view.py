"""
This module contains the function to get the left view of a binary tree.
"""


class Node:
    """
    Class to represent the Node in binary tree hierarchy with pointers to it's
        left and right children if any
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_node = left
        self.right_node = right


def get_left_view(current_node, visible_nodes, visited_levels=None, current_level=0):
    """
    Args:
        current_node (Node): Instance of Node class.
        visible_nodes (list): List of visible node values.
        visited_levels (set, optional): Set of visited levels so far.  Default is empty set.
        current_level (int, optional): Current level number being visited. Default is 0.
    Returns:
        list: Node values visible from left side, starting from root node value towards left
                visible node values downwards.

    Raises:
        ValueError:
            - When invalid value for visible_nodes is provided.
            - When invalid value for current_node is provided.
            - When invalid value for current_level is provided.
            - When invalid value for visited_levels is provided.
    """
    if not isinstance(visible_nodes, list):
        raise ValueError("'visible_nodes' should be of type list")

    if not (visited_levels is None or isinstance(visited_levels, set)):
        raise ValueError("'visited_levels' should be of type set")

    if not isinstance(current_level, int):
        raise ValueError("'current_level' should be of type int")

    if not current_node or not isinstance(current_node, Node):
        raise ValueError("'current_node' should be instance of Node class")

    visited_levels = visited_levels or set()

    if current_level not in visited_levels:
        visible_nodes.append(current_node.value)
        visited_levels.add(current_level)
    if current_node.left_node:
        get_left_view(
            current_node.left_node, visible_nodes, visited_levels, current_level + 1
        )
    if current_node.right_node:
        get_left_view(
            current_node.right_node, visible_nodes, visited_levels, current_level + 1
        )

    return visible_nodes
