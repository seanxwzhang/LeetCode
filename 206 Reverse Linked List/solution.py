# Reverse a singly linked list.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            nex = head.next
            head.next = prev
            prev = head
            head = nex
        return prev

