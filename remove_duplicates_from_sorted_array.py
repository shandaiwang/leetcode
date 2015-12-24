# -*- encoding=utf-8 -*-
__author__ = 'lixianpeng'


"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        和之前一个元素不相同，即可
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        index = 1   # 不确定元素的index
        for i in range(1, len(nums)):
            if nums[index - 1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index

    def removeDuplicates2(self, nums):
        """
        和之前一个元素不相同，即可
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        index = 0   # 需要比较的元素的index
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1

solution = Solution()
print(solution.removeDuplicates2([1, 1, 1, 1, 2, 2, 3, 3]))