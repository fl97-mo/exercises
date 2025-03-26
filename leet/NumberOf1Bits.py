#191. Number of 1 Bits
#Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
#Example 1:
#Input: n = 11
#Output: 3
#Explanation:
#The input binary string 1011 has a total of three set bits.

def hammingWeight(n):
    bit_counter = 0
    while n > 0:
        bit = n % 2
        n = n // 2
        if bit == 1:
            bit_counter +=1    
    return bit_counter

print(hammingWeight(13))    
