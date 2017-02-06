// Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    if (!l1) return l2;
    else if (!l2) return l1;
    var head = (l1.val < l2.val) ? l1 : l2;
    var res = head;
    if (l1.val < l2.val)
        l1 = l1.next;
    else
        l2 = l2.next;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            head.next = l1;
            l1 = l1.next;
        } else {
            head.next = l2;
            l2 = l2.next
        }
        head = head.next;
    }
    if (l1)
        head.next = l1;
    if (l2)
        head.next = l2;
    return res;
};