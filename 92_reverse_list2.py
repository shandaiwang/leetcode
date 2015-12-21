__author__ = 'pld'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head, m, n):
    """
    :param head: ListNode
    :param m: int
    :param n: int
    :return: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    before = dummy
    for i in range(m - 1):
        if before is None:
            return head
        before = before.next

    current = start = before.next
    if start is None:
        return head
    before.next = None
    for i in range(n - m + 1):
        if current is None:
            break
        next = current.next
        current.next = before.next
        before.next = current
        current = next
    start.next = current
    return dummy.next

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = reverse_list(node1, 4, 3)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
