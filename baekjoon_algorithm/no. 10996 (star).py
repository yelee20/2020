n = int(input())
first = (n+1)//2 #number of stars in the first row
second = n - first #number of stars in the second row
for i in range (n):
  print("* "*first)
  print(" *"*second)

#if input is 2
#* 
# *
#*
# *

#if input is 3
#* *
# *
#* *
# *