__author__ = 'pld'


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
        index_dict.setdefault(nums[i], i)
    return []

print(two_sum([2, 3, 4], 6))