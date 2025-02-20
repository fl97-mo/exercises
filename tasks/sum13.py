#Return the sum of the numbers in the array, returning 0 for an empty array. 
#Except the number 13 is very unlucky, so it does not count 
#and numbers that come immediately after a 13 also do not count.

#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    sums = 0
    thirteen = False
    for i in range(len(nums)):
        if thirteen == True:
            thirteen = False
            continue
        if nums[i] == 13:
            thirteen = True
            continue
        else:
            sums += nums[i]
        
    return sums

print(sum13([13, 1, 2, 13, 2, 1, 13])) #3