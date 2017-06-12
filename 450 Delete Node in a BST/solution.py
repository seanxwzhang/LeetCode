#!/usr/bin/env python
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7


# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def deleteNode(self, root, key):
        dummy = TreeNode(sys.maxsize)
        dummy.left = root
        self.helper(dummy, True, key)
        return dummy.left
        
    
    def helper(self, parent, left, key):
        tree = parent.left if left else parent.right
        if not tree:
            return parent
        elif key > tree.val:
            self.helper(tree, False, key)
        elif key < tree.val:
            self.helper(tree, True, key)
        else: # there is a match
            if not tree.left and not tree.right:
                if left: parent.left = None
                else: parent.right = None
            elif not tree.left:
                if left: parent.left = tree.right
                else: parent.right = tree.right
            elif not tree.right:
                if left: parent.left = tree.left
                else: parent.right = tree.left
            else: # if there is a left subtree and right subtree, find the inorder successor
                successor = tree.right
                while successor.left:
                    successor = successor.left
                tree.val = successor.val
                tree.right = self.deleteNode(tree.right, successor.val)
        return parent



        