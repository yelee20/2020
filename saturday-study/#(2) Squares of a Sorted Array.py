#20200614 leetcode (easy)
#Given an array of integers A sorted in non-decreasing order, 
#return an array of the squares of each number, also in sorted non-decreasing order.

#Input: [-4,-1,0,3,10]
#Output: [0,1,9,16,100]

class Solution(object):
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i]**2
        A = sorted(A)
        return A