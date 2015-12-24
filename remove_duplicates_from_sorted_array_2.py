# -*- encoding:utf-8 -*-

__author__ = 'lixianpeng'


"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        只需要和隔一个的前一个不相等即可
        :type nums: List[int]
        :rtype: int
        """
        index = 2   # 待确定元素的index
        for i in range(2, len(nums)):
            if nums[index - 2] != nums[i]:
                nums[index] = nums[i]
                index += 1  # 下一个要确定的元素index
        return index


    def removeDuplicates2(self, nums):
        """
        只需要和隔一个的前一个不相等即可
        :type nums: List[int]
        :rtype: int
        """
        index = 0   # 已知需要比较的index
        for i in range(2, len(nums)):
            if nums[index] != nums[i]:
                index += 1  # 下一个需要比较的index
                nums[index + 1] = nums[i]
        return index + 2
solution = Solution()
print(solution.removeDuplicates2([1, 1, 1]))