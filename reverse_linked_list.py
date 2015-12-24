__author__ = 'pld'


import linkutils

"""
Reverse a singly linked list.
"""


def reverse_list(head):
    """
    :param head: ListNode
    :return: ListNode
    """
    sentinel = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = sentinel
        sentinel = current
        current = next_node
    return sentinel

head = reverse_list(linkutils.parse_array_2_list([0, 1, 2, 3, 4]))
linkutils.iterate_linked_list(head)
