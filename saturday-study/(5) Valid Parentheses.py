# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        
        B2 = ['()','{}','[]']

        for i in range(len(s)-1):
            for ele in B2:
                if ele in s:
                    s = s.replace(ele,'')
        
        if len(s) == 0:
            return True
        else:
            return False