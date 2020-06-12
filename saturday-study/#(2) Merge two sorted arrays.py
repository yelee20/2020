#2. merge two sorted arrays
#Write a function that accepts two sorted arrays of numbers
#return a combined array of the numbers in sorted order
#The optimal solution is O(n) linear time, if you get stuck you can research ‘merge sort’
#input: [3, 4, 7, 8] [1, 5, 6, 9]
#output: [1, 3, 4, 5, 6, 7, 8, 9]

def mergearrays (arr1,arr2):
    if len(arr1)>1:
        left_1 = arr1[:len(arr1)//2]
        right_1 = arr1[len(arr1)//2:]
    elif len(arr2)>1:
        left_2 = arr2[:len(arr2)//2]
        right_2 = arr2[len(arr2)//2:]

    return right_1

print(mergearrays([3, 4, 7, 8], [1, 5, 6, 9]))