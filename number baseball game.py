#python3
#generate three random integers without duplicates (0 ~ 9)
import random
computer_num = random.sample(range(0,9),3)
    
#get input (three integers) from users
input_num = list(map(int,input("Guess three different integers (range: 0~9) \n ex) 3 6 7").split()))[:3]

""">>>>>>>>filter invalid inputs
for i in range (0,2):
    if input_num[i-1]==input_num[i]:
        break
    print("You have duplicates! Try again!")"""

print(computer_num)
#Initialize number of balls and strikes
B=0 #number of balls
S=0 #number of strikes

#Update B and S
for i in range (0,3):
    if computer_num[i] == input_num[i]:
        S += 1
    for j in range (0,3):
        if i!=j and computer_num[i] == input_num[j]:
            B += 1

#Check if the user get same numbers or not
while S != 3:
    if B==0 and S==0:
        print("Out!")
    else:
        print("Your input was ",input_num,"\n")
        print("You got ",B,"Ball(s)\n")
        print("You got ",S,"Strike(s)")
    
    input_num=[]
    input_num = list(map(int,input("Guess three different integers (range: 0~9) \n ex) 3 6 7").split()))[:3]

    #initialize number of balls and strikes
    B=0 #number of balls
    S=0 #number of strikes
    
    for i in range (0,3):
        if computer_num[i] == input_num[i]:
            S += 1
        for j in range (0,3):
            if i!=j and computer_num[i] == input_num[j]:
                B += 1
else:
    print("Three strikes!")