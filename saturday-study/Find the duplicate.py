# No. 1
#Write a function called findTheDuplicate which accepts an array of numbers containing a single duplicate. 
#The function returns the number which is a duplicate or undefined if there are no duplicates.


def findTheDuplicate(arr):
    duplicate=[]

    for i in range(len(arr)):
      for j in range(len(arr)):
       if arr[i] == arr[j] and i!=j:
        duplicate.append(arr[i])

    if len(duplicate)==0:
       return ("undefined")
    else:
       print(*set(duplicate)) #remove brackets

print(findTheDuplicate([1,2,1,4,3,12])) #1
print(findTheDuplicate([6,1,9,5,3,4,9])) #9
print(findTheDuplicate([2,1,3,4])) #undefined