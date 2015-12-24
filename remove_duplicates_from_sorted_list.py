__author__ = 'pld'

import linkutils

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

class Solution(object):
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = head
        node = head
        while node:
            if node.val != sentinel.val:
                sentinel.next = node
                sentinel = node
            node = node.next
        if sentinel:
            sentinel.next = None
        return head


    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

solution = Solution()
head = linkutils.parse_array_2_list([1, 2, 3, 3, 3])

solution.deleteDuplicates2(head)
linkutils.iterate_linked_list(head)