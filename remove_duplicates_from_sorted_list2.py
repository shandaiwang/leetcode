__author__ = 'pld'

import linkutils


# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        new_head = sentinel = linkutils.ListNode(head.val - 1)
        pre = new_head
        node = head
        while node:
            next = node.next
            if node.val != pre.val:
                if not next or next.val != node.val:
                    sentinel.next = node
                    sentinel = node
                    sentinel.next = None
            pre = node
            node = next
        return new_head.next

head = linkutils.parse_array_2_list([1,2,2])
solution = Solution()
head = solution.deleteDuplicates(head)
linkutils.iterate_linked_list(head)