#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.
#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1

def searchInsert(nums, target):

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif len(nums) > 1 and nums[i] <= target <= nums[i+1]:
                return i + 1
            elif nums[0] > target:
                return 0
            elif nums[-1] < target:
                return len(nums)

print(searchInsert([1,3,5,6],7))
