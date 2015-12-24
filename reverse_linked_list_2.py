__author__ = 'pld'


import linkutils

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
"""


def reverse_list(head, m, n):
    """
    :param head: ListNode
    :param m: int
    :param n: int
    :return: ListNode
    """
    before = dummy = linkutils.ListNode(-1)
    dummy.next = head
    for i in range(m - 1):
        if before is None:
            return head
        before = before.next

    current = start = before.next
    if start is None:
        return head
    before.next = None
    j = 0
    for i in range(n - m + 1):
        if current is None:
            break
        next = current.next
        current.next = before.next
        before.next = current
        current = next
    start.next = current
    return dummy.next


head = reverse_list(linkutils.parse_array_2_list([0, 1, 2, 3, 4]), 3, 4)
linkutils.iterate_linked_list(head)
