#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    common =  strs[0]

    for word in strs[1:]:
        while not word.startswith(common):
            common = common[:-1]
        if len(common) < 1:
            return ""
    return common

print(longestCommonPrefix(["flower","flow","flight"]))