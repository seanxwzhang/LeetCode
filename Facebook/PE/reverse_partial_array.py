def partial_reverse(arr, i, j):
    start, end = min(i, j), max(i, j)
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def partial_reverse_linked_list(head, i, j): #suppose 0-based
    dummy = ListNode()
    dummy.next = head

    ith_prev, ith, jth = dummy, head, head
    for x in xrange(0, j+1):
        if x == i - 1:
            ith_prev = head
        elif x == j:
            jth = head
        if head.next:
            head = head.next
        else:
            raise ValueError("None in linked list")
    ith = ith_prev.next
    jth_next = jth.next

    jth.next = None
    reverse(ith)
    ith_prev.next = jth
    ith.next = jth_next

    return dummy.next

def reverse(head):
    prev = None
    while head:
        n = head.next
        head.next = prev
        prev = head
        head = n
