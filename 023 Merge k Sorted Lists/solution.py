# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        ind, cur = 0, None
        while (ind < len(lists)):
            left, right, dummy = cur, lists[ind], ListNode(0)
            dummy_head = dummy
            while(left and right):
                if (left.val < right.val):
                    dummy.next = left
                    left = left.next
                else:
                    dummy.next = right
                    right = right.next
                dummy = dummy.next
            if (left):
                dummy.next = left
            if (right):
                dummy.next = right
            cur = dummy_head.next
            ind += 1
        return cur

if __main__ == "__main__":
    s = Solution()
    
        