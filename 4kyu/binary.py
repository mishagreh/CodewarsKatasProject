# https://www.codewars.com/kata/52bef5e3588c56132c0003bc
#
# You are given a binary tree:
#
# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
#
# Your task is to return the list with elements from tree sorted by levels,
# which means the root element goes first, then root children
# (from left to right) are second and third, and so on.
#
# test.assert_equals(tree_by_levels(None), [])
# test.assert_equals(tree_by_levels(
# Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5),
# Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])
#
# Return empty list if root is None.
# def tree_by_levels(node):
# return
import pdb


class Node(list):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


def tree_by_levels(node):
    if node is None:
        return []

    res = []
    queue = []
    # breakpoint()

    # Enqueue Root and initialize height
    queue.append(node)

    while (len(queue) > 0):

        breakpoint()
        # Print front of queue and
        # remove it from queue
        res.append(queue[0].value)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

    print(res)
    return res


node = Node(Node(Node(Node(None, None, 5), Node(None, None, 6), 4), None, 1),
            Node(None, None, 2), 3)
tree_by_levels(node)
