__author__ = 'pld'


def single_number_2(nums):
    """
    :param nums: List[int]
    :return: int
    """
    ones, twos = 0, 0
    for num in nums:
        twos ^= (ones & num)
        ones ^= num
        mask = ~(ones & twos)
        twos &= mask
        ones &= mask
    return ones


print(single_number_2([1, 2, 1, 3, 2, 1, 2]))