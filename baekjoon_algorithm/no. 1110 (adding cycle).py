N = NewN =int(input()) #input value
Cycle = 0 #Number of Cycle
while (NewN!= N or Cycle == 0):
    first_d = NewN%10 #value of the first digit
    tenth_d = NewN//10 # value of the tenth digit
    sum_d = first_d+tenth_d # sum of first digit and tenth digit
    NewN=(sum_d)%10+(first_d)*10
    Cycle+=1

print(Cycle)