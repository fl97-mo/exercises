#You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
#Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#Letters are case sensitive, so "a" is considered a different type of stone from "A".


class Solution(object):
    def numJewelsInStones(jewels, stones):

        dict = {}
        counter = 0
        for letter in jewels:
            dict.setdefault(letter, 0)
        for letter in stones:
            if letter in dict:
                counter += 1
                
        return counter
    
    
    print(numJewelsInStones("aA","aAAbbbb")) 