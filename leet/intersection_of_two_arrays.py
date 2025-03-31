#Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must be unique and you may return the result in any order.
#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
def intersection(nums1, nums2):
    nums = []
    
    for i in nums2:
        if i in nums1 and i not in nums:
            nums.append(i)
        else:
            continue
    
    return nums

print(intersection([1,2,2,1],[2,2]))