# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        track = head
        # create a duplicate for every node after the node
        while(track):
            newNode = RandomListNode(track.label)
            tmp = track.next
            newNode.next = tmp
            track.next = newNode
            track = tmp
        # add random pointer to every node
        track = head
        while(track and track.next):
            if (track.random):
                track.next.random = track.random.next
            track = track.next.next
        # extract the duplicate list
        res = head.next
        while(head and head.next):
            dup = head.next
            head.next = dup.next
            if head.next:
                dup.next = head.next.next
            head = head.next
        return res

if __name__ == "__main__":
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    s = Solution()
    res = s.copyRandomList(node1)
    