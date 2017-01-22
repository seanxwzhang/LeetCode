class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

r = ListNode(0)
t = r
t.val = 2
print(r.val)
