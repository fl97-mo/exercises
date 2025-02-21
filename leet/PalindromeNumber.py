#given an integer x, return true if x is a palindrome, and false otherwise.
#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return (x == x[::-1] and x >= 0)
             