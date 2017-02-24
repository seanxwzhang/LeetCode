#! /usr/bin/env python
# Sort a linked list in O(n log n) time using constant space complexity.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# a merge sort implementation
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now slow reaches the middle of the list
        mid = slow.next
        slow.next = None
        sorted_head = self.sortList(head)
        sorted_mid = self.sortList(mid)
        # now two sub lists are sorted, sort them in O(n)
        dummyNode = ListNode(0)
        track = dummyNode
        while sorted_head and sorted_mid:
            if sorted_head.val < sorted_mid.val:
                track.next = sorted_head
                sorted_head = sorted_head.next
            else:
                track.next = sorted_mid
                sorted_mid = sorted_mid.next
            track = track.next
        if sorted_head: track.next = sorted_head
        if sorted_mid: track.next = sorted_mid
        return dummyNode.next
        