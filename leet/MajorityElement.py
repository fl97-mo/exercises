#The majority element is the element that appears more than ⌊n / 2⌋ times.
#You may assume that the majority element always exists in the array.
#example 1:
#Input: nums = [3,2,3]
#Output: 3

def majorityElement(nums):
    dict = {}
    for i in nums:
        dict[i] = dict.get(i,0) +1
        
        
    return max(dict.keys(), key=lambda x: dict[x])
    
print(majorityElement([6,5,5]))