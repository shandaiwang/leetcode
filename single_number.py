__author__ = 'pld'


from functools import reduce
from operator import xor


def single_number(nums):
    """
    :param nums: List[int]
    :return: int
    """
    return reduce(xor, nums)

print(single_number([1, 2, 3, 1, 2, 3, 4]))