# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        if headA == headB:
            return headA
        headC = headA
        while headC.next:
            headC = headC.next
        headC.next = headA
        slow, fast = headB, headB
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if (not fast.next) or (not fast.next.next): 
            headC.next = None
            return None
        fast = headB
        while fast != slow:
            fast = fast.next
            slow = slow.next
        headC.next = None
        return slow

    def betterSolution(self, headA, headB)
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa