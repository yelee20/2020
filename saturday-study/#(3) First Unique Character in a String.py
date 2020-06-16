# ※Time Limit Exceeded in leetcode
#20200620 leetcode (easy) no.387
#1. Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

#Ex1) 
#s = "leetcode"
#return 0.

#Ex2)
#s = "loveleetcode",
#return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        split_word = list(s) #separate characters
        result = -1
        for i in range(len(split_word)):
                if split_word.count(split_word[i])==1:
                    result = i
                    break
        return result