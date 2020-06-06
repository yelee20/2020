ABC = list(int(num) for num in input().strip().split())[:3] #get list input
min_value = min(ABC) #get a minimum value of items in a list
ABC.remove(min_value) #remove it
max_value = max(ABC) #get a maximum value of items in a list
ABC.remove(max_value) #remove it
print(*ABC, sep = " ") #print the second biggest item (without brackets)