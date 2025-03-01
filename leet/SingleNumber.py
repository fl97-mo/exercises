#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.


def singleNumber(nums):

    nums_dict = {}

    for i in nums:
        nums_dict[i] = nums_dict.get(i, 0) + 1

    for key, value in nums_dict.items():
        if value == 1:
            return key


print(singleNumber([2,2,3,3,1]))