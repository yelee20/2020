n = int(input())
star = 2*n-1 #number of *
space = 0 #number of " "
for i in range(2*n-1):
  if i <= n-1 and i > 0:
    star -= 2
    space += 1
  elif i > n-1:
    star += 2
    space -= 1
  print(' '*space + '*'*star)