# [1,2,3,5,8,11,14,36,89,123,567] | where is 89?

def binarySearch(numbers, item):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == item:
            return mid
        elif item > numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
        
    return "not in list"
        
print(binarySearch([1,2,3,5,8,11,14,36,89,123,567], 89))
