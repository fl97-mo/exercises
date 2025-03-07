#Longest Substring Without Repeating Characters
#Given a string s, find the length of the longest substring without duplicate characters.
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    list_chars = []
    length = 0

    for i in range(len(s)):
        list_chars = []
        for j in range(i, len(s)):
            if s[j] in list_chars:
                break
            list_chars.append(s[j])
            length = max(length, len(list_chars))

    return length

print(lengthOfLongestSubstring("pwwkew"))