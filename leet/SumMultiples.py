#Given a positive integer n, find the sum of all integers in the range [1, n]
# inclusive that are divisible by 3, 5, or 7.
#Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
#Example 1:
#Input: n = 7
#Output: 21
#Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. 
#The sum of these numbers is 21.


def sumOfMultiples(n):
    sum = 0

    for number in range(n+1):
        if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            sum = sum + number

    return sum

print(sumOfMultiples(7))