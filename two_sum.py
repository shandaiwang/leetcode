__author__ = 'pld'


"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


def two_sum(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    index_dict = {}
    for i in range(len(nums)):
        index = index_dict.get(target - nums[i])
        if index is not None:
            return [index + 1, i + 1]
        index_dict[nums[i]] = i
    return []

print(two_sum([2, 3, 4], 6))