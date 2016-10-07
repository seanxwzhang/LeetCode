class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        prev = head
        carrier, remainder = 0, 0

        while l1 or l2 or carrier:
            cur = ListNode(0)
            i1 = 0 if (l1 == None) else l1.val
            i2 = 0 if (l2 == None) else l2.val
            sum = i1 + i2 + carrier
            cur.val = sum % 10
            carrier = sum / 10
            prev.next = cur
            prev = cur

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            

        return head.next
