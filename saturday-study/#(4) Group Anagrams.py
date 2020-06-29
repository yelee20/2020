#20200627 leetcode (easy)
#Given an array of strings, group anagrams together.

#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

def groupAnagrams(arr):
    temp = []
    result = []
    for i in range(len(arr)):
        temp.append(sorted(list(arr[i]))) #split str into char
        for j in range(i+1, len(temp)):
            print(temp[i])
            if temp[i] == temp[j]:
                result.append(arr[i])

        
    return temp

groupAnagrams(["eat","tea", "tan", "ate", "nat", "bat"])




"""for j in range(len(arr)):
        for k in range(len(temp[j])):
            temp[j][k] = ord(temp[j][k])  
        sorted(temp[j])"""