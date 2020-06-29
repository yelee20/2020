#Write a function that takes two non-empty arrays of integers, finds the pair of numbers (one from ea. array)
#whose absolute difference is closest to zero, and returns an array containing the pair.
#Assume there is only one pair with the smallest difference.


    def setup(arr1, arr2):                              #get two arrays

        diff = []
        pair = []

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                absDiff = abs(arr1[i]-arr2[j])         #absolute difference
                diff.append(absDiff)                   
                if diff[i*(len(arr2))+j] == min(diff):  
                        pair.clear()                    #remove all elements
                        pair.extend((arr1[i],arr2[j]))  #add pair
        return pair
    
    setup([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17])
    #expected output = [28,26]

    setup([-1, 1000, 28], [28, 134, 135, 15])
    #expected output = [28, 28]

    setup([-1], [29, 134, 135, -20])
    #expected output = [-1, -20]