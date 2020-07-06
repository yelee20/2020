#20200711 leetcode (easy)
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, 
# and all letters reverse their positions.

#Example 1
#Input: "ab-cd"
#Output: "dc-ba"

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        nL = {}
        new = S
        for i in range(len(S)):
            #take out the non-letter characters
            if S[i].isalpha() == False: #isalpha checks if the string only contains letters or not
                nL[i] = S[i]  
                new = new.replace(S[i],'')
        #reverse all letters
        new = list(reversed(new))
        #insert the non-letter characters
        for j in nL.keys():
            new.insert(j,nL.get(j))
        
        #change the list to a string
        new = ''.join(new)
        return new

#time complexity: O(2N)