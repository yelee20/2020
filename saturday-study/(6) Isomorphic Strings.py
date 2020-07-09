# 202007011 leetcode (easy)
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        nS = list(s)
        nT = list(t)
        sn = {}
        result=[]
        
        for i in range(len(nT)):
            sn[nS[i]] = nT[i]
        keys = list(sn.keys())
        values = list(sn.values())
        
        for k in range(len(nS)):
            if k< len(values) and values.count(values[k]) > 1:
                return False
            elif nS[k] in keys:
                result.append(sn.get(nS[k]))
        result = ''.join(result)
        
        if result == t:
            return True
        else:
            return False

#time complexity: O(N**2)