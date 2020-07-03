#20200704 leetcode (easy)
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example 1
# Input: Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# Output: [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        for i in range(len(nums)*(len(nums)-1)//2):
            if nums[p1] + nums[p2] == target:
                return [p1,p2]
            elif p2 >= len(nums)-1:
                p1+=1
                p2 = p1 + 1
            else:
                p2 += 1
           
            #len(nums) = 6, run 5+4+3+2+1 = 15 times
            #len(nums) = 5, run 4+3+2+1 = 10 times   
            #len(nums) = 4, run 3+2+1 = 6 times
            #len(nums) = 3, run 2+1 = 3 times



"""
Method(2) Nested for loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]"""