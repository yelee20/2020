class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        max_substring = 0
        for ele in s:
            if ele == "R":
                cnt += 1 # add 1 if the element is R
            elif ele == "L":
                cnt -= 1 # substract 1 if the element is L
            if cnt == 0:
                max_substring += 1
        return max_substring