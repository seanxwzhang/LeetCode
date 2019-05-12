# Construct Tree from given Inorder and Preorder traversals
# Let us consider the below traversals:

# Inorder sequence: D B E A F C
# Preorder sequence: A B D E C F

# Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
# In a Preorder sequence, leftmost element is the root of the tree. So we know ‘A’ is root for given sequences. By searching ‘A’ in Inorder sequence, we can find out all elements on left side of ‘A’ are in left subtree and elements on right are in right subtree. So we know below structure now.

#                  A
#                /   \
#              /       \
#            D B E     F C
# We recursively follow above steps and get the following tree.

#          A
#        /   \
#      /       \
#     B         C
#    / \        /
#  /     \    /
# D       E  F
# Algorithm: buildTree()
# 1) Pick an element from Preorder. Increment a Preorder Index Variable (preIndex in below code) to pick next element in next recursive call.
# 2) Create a new tree node tNode with the data as picked element.
# 3) Find the picked element’s index in Inorder. Let the index be inIndex.
# 4) Call buildTree for elements before inIndex and make the built tree as left subtree of tNode.
# 5) Call buildTree for elements after inIndex and make the built tree as right subtree of tNode.
# 6) return tNode.
from typing import List
from pprint import pprint
from collections import deque


class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# # Breadth first traversals
# def printTree(root):
#     queue = deque()
#     node = root
#     while queue or node:
#         if len(queue):
#             p = queue.pop()
#             print()

def buildTree(inorder: List[str], preorder: List[str]):
    assert len(inorder) == len(preorder), "length must be the same"
    if not inorder:
        return None
    root = BstNode(preorder[0])
    index = inorder.index(root.key)
    root.left = buildTree(inorder[0:index], preorder[1:index + 1])
    root.right = buildTree(inorder[index + 1:], preorder[index + 1:])
    return root

root = buildTree(list('DBEAFC'), list('ABDECF'))
root.display()
