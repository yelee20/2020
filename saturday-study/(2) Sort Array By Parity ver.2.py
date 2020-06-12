#20200614 leetcode (easy)
#Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#You may return any answer array that satisfies this condition.

#Input: [4,2,5,7]
#Output: [4,5,2,7]
#Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

class Solution(object):
    def sortArrayByParityII(self, A):
        odd_arr = []
        even_arr = []
        result = []
        M = len(A)

        for i in range(M):  
            if A[i]%2 != 0:              #odd
                odd_arr.append(A[i])
            else:                        #even
                even_arr.append(A[i])

        for j in range(M//2):
            result.append(even_arr[j])
            result.append(odd_arr[j])

        return result