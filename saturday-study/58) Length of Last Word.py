class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        loc = s.rfind(" ") #find the location of space
        new_s = s.replace(" ","") #remove space
        if len(new_s) == 0:
            return 0
        else:
            while s[len(s)-1] == ' ':
                s = s[:len(s)-1]
            loc = s.rfind(" ")
            s = s[loc+1:]
            result = len(s)
            return result