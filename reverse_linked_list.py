__author__ = 'pld'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = reverse_list(node1)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
