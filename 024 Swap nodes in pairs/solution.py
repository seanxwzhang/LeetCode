#!/usr/bin/env python
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """this class blablabla"""
    def swapPairs(self, head):
        """this function blablabla"""
        if not head or not head.next:
            return head
        res, prev = head.next, None
        while head and head.next:
            nex = head.next.next
            if prev:
                prev.next = head.next
            head.next.next = head
            head.next = nex
            prev = head
            head = nex
        return res
    def printNodes(self, head):
        while head:
            print('{0} '.format(head.val))
            head = head.next

if __name__ == '__main__':
    nodes = [ListNode(count) for count in xrange(6)]
    for idx, node in enumerate(nodes[:-1]):
        node.next = nodes[idx + 1]
    s = Solution()
    s.printNodes(nodes[0])
    print("=========")
    s.printNodes(s.swapPairs(nodes[0]))

    