#20200614
# 1. bubble sort
# given an array of numbers, sort them without using your language’s built in .sort method
# input: [4, 7, 2, 3, 8]
# output: [2, 3, 4, 7, 8]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble_sort([4, 7, 2, 3, 8]))