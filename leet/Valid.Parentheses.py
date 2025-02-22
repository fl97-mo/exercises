#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Example 1:
#Input: s = "()"
#Output: true
#Example 2:
#Input: s = "()[]{}"
#Output: true
def isValid(s):
    while any(pair in s for pair in ["()", "[]", "{}"]):
        for pair in ["()", "[]", "{}"]:
            s = s.replace(pair, "")
    return s == ""


print(isValid("()[]{}"))