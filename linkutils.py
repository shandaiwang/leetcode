# -*- coding:utf-8 -*-
__author__ = 'pld'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def parse_str_2_list(chars):
    """
    将字符串解析成链表
    :param chars:
    :return:
    """
    sentinel = ListNode(-1)
    head = sentinel
    for val in chars.split('->'):
        node = ListNode(int(val))
        sentinel.next = node
        sentinel = node
    return head.next


def parse_array_2_list(nums):
    """
    将字符串解析成链表
    :param nums:
    :return:
    """
    sentinel = ListNode(-1)
    head = sentinel
    for num in nums:
        node = ListNode(num)
        sentinel.next = node
        sentinel = node
    return head.next


def iterate_linked_list(head):
    """
    遍历链表
    :param head:
    :return:
    """
    node = head
    while node:
        print(node.val)
        node = node.next