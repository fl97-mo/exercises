#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False

def has22(nums):
    string = ""
    for i in nums:
        string+= str(i)
    return("22" in string)

print(has22([1, 2, 2]))