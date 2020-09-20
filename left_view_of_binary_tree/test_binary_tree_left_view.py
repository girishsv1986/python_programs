"""
This module tests the function to get the left view of a binary tree.
"""
import unittest

from binary_tree_left_view import Node, get_left_view


class TestBinaryTreeLeftView(unittest.TestCase):
    """
    Contains the unittests for "get_left_view" function
    """

    def test_node_instance_validation(self):
        """
        Test "get_left_view" function raises the ValueError exception when current_node param
            is not instance of Node class
        """
        expected_error_message = "'current_node' should be instance of Node class"
        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(None, [])
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view([], [])
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(object, [])
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view({}, [])
        self.assertEqual(expected_error_message, str(exc.exception))

    def test_visible_nodes_validation(self):
        """
        Test "get_left_view" function raises the ValueError exception when visible_nodes param
            is not list
        """
        expected_error_message = "'visible_nodes' should be of type list"
        node_instance = Node("A")
        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, "")
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, {})
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, set())
        self.assertEqual(expected_error_message, str(exc.exception))

    def test_current_level_validation(self):
        """
        Test "get_left_view" function raises the ValueError exception when current_node param
            is not int
        """
        expected_error_message = "'current_level' should be of type int"
        node_instance = Node("A")
        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, [], current_level="")
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, [], current_level=[])
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, [], current_level={})
        self.assertEqual(expected_error_message, str(exc.exception))

    def test_visited_levels_validation(self):
        """
        Test "get_left_view" function raises the ValueError exception when visited_levels param
            is provided is not of type set
        """
        expected_error_message = "'visited_levels' should be of type set"
        node_instance = Node("A")
        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, [], visited_levels="")
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, [], visited_levels=[])
        self.assertEqual(expected_error_message, str(exc.exception))

        with self.assertRaises(ValueError) as exc:
            _ = get_left_view(node_instance, [], visited_levels=False)
        self.assertEqual(expected_error_message, str(exc.exception))

    def test_get_left_view_with_root_node(self):
        """
        Test "get_left_view" function return value when binary tree has
            only one node i.e. root node
        In this case function should return root node value in list as left view
        """
        root = Node("A")
        visible_nodes = get_left_view(root, [])
        self.assertEqual(visible_nodes, ["A"])

    def test_get_left_view_with_complete_binary_tree(self):
        """
        Test "get_left_view" function return value when binary tree has
            both left and right nodes
        In this case function should return list of visible nodes

        eg:
            A
           / \
          B   C
         / \ / \
        D  E F G
        """
        node_d = Node("D")
        node_e = Node("E")
        node_f = Node("F")
        node_g = Node("G")

        node_b = Node("B", node_d, node_e)
        node_c = Node("C", node_f, node_g)

        node_a = Node("A", node_b, node_c)
        visible_nodes = get_left_view(node_a, [])
        self.assertEqual(visible_nodes, ["A", "B", "D"])

    def test_get_left_view_with_long_right_nodes_binary_tree(self):
        """
        Test "get_left_view" function return value when binary tree right side has
            more levels compared with left side of binary tree.
        In this case function should return list of visible nodes

        eg:
            10
           / \
         20    30
          \    /
          40  50
               \
                60
               / \
              70 80
        """
        root = Node(10)
        root.left_node = Node(20)
        root.right_node = Node(30)
        root.left_node.right_node = Node(40)
        root.right_node.left_node = Node(50)
        root.right_node.left_node.right_node = Node(60)
        root.right_node.left_node.right_node.left_node = Node(70)
        root.right_node.left_node.right_node.right_node = Node(80)
        visible_nodes = get_left_view(root, [])
        self.assertEqual(visible_nodes, [10, 20, 40, 60, 70])


if __name__ == "__main__":
    unittest.main()
