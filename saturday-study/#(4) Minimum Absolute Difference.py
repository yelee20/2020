#20200627 leetcode (easy)
#Given an array of distinct integers arr, find all pairs of elements 
#with the minimum absolute difference of any two elements. 

#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    #a, b are from arr
    #a < b
    #b - a equals to the minimum absolute difference of any two elements in arr

def minimumAbsDifference(arr):
    pairs = []
    diff = []
    location = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            absDiff = abs(arr[i]-arr[j])
            diff.append(absDiff)

            if diff[location] == min(diff):
                pairs.append([arr[i],arr[j]])
                location += 1
    
    sorted(pairs)
    return pairs

minimumAbsDifference([4,2,1,3]) 

#i 0 0 0 1 1
#j 1 2 3 0 1
#r 0 1 2 3 4