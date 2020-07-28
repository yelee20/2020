class Solution:
    def findLHS(self, nums: List[int]) -> int:
        no_dup = list(set(nums))
        no_dup.sort()
        diff_one = []
        lst_length = []
        
        for i in range(len(no_dup)-1):
            if abs(no_dup[i+1] - no_dup[i]) == 1:
                diff_one.append(no_dup[i])
                
        for i in diff_one:
            temp = nums.count(i) + nums.count(i+1)
            lst_length.append(temp)
        
        if len(lst_length) == 0:
            return 0
        else:
            return max(lst_length)