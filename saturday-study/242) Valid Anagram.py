class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif len(s) == len(t):
            s = list(s)
            t = list(t)
            sNum = []
            tNum = []
            for i in range(len(s)):
                sNum.append(ord(s[i]))
                tNum.append(ord(t[i]))
            sNum.sort()
            tNum.sort()
            if sNum == tNum:
                return True
            else:
                return False