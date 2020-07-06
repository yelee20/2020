#20200704 Leetcode (medium)
#Given a string, find the length of the longest substring without repeating characters.

# Example 1
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2
# Input: "dvdf"
# Output: 3
# Explanation: The answer is "vdf", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = [] #store non-repeating characters
        cnt = [0]   #store the length of the list 'result'
                    #added 0 for an empty input ""
    #s = advdf
    #ele =
    #result = []
    #cnt = []

        for ele in s:
            if ele not in result:
                result.append(ele)
            elif ele in result:
                del result[:result.index(ele)+1]
                result.append(ele)
            cnt.append(len(result)) 
                             
        return max(cnt)