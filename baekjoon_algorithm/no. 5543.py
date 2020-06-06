burger_p = []
drink_p = []
price_list = []
for i in range(3):
  burger_p.append(int(input())) #get prices of burgers
for i in range(2):
  drink_p.append(int(input())) #get prices of drinks

for i in burger_p:
  for j in drink_p:
    price_list.append(i+j)  #sum up

min_p = min(price_list)
final_p = min_p - 50
print(final_p)
