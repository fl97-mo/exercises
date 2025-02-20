def twoSum(nums, target):
        seen = {}  # speichert: Zahl -> Index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        
        
        
twoSum([9,8,7,6,5,4,3,2,1,0],11)    