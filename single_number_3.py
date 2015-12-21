#
from functools import reduce
from operator import xor


def single_number_3(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    xor_res = reduce(xor, nums)
    mask = xor_res & (-xor_res)
    # a = reduce(xor, (num for num in nums if num & mask))
    a = reduce(xor, filter(lambda x: x & mask, nums))
    return [a, a ^ xor_res]

print(single_number_3([1, 2, 3, 1, 2, 3, 4, 5]))