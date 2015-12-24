__author__ = 'lixianpeng'


"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first_index = 0
        last_index = len(nums) - 1
        mid_index = int(last_index / 2)
        while first_index < last_index:
            mid = nums[mid_index]
            if target == mid:
                return mid_index
            elif target > mid:
                first = nums[first_index]
                last = nums[last_index]
                if last > mid:
                    pass
                else:
                    pass

            elif target < mid:
                pass
        return -1

solution = Solution()
print(solution.search([3, 4, 5, 6, 1, 2], 5))