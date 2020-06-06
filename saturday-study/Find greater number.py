# No. 2
#Write a function called findGreaterNumbers which accepts an array and returns the number of times a number is followed by a larger number. 
#Note that the numbers don't need to be next to each other in the array. 
#Any pair where the second number comes later in the array and is also the larger number should count.

def findGreaterNumbers(arr):
  count=0
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i]<arr[j] and i<j: #if a number is followed by a larger number
        count+=1

  return count
      
print(findGreaterNumbers([1,2,3])) # 3 (2 > 1, 3 > 2, and 3 > 1)
print(findGreaterNumbers([6,1,2,7])) # 4
print(findGreaterNumbers([5,4,3,2,1])) # 0
print(findGreaterNumbers([])) # 0