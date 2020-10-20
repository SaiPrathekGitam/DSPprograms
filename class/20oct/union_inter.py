# 8. Find the Union and Intersection of the two sorted arrays
l1 =  list(map(int, input('Enter List Elements : ').split()))
l2 =  list(map(int, input('Enter List Elements : ').split()))
inter = []
uni = l1.copy()
for i in l2:
  for j in uni:
    if i==j:
      break
  else:
    uni.append(i)
for i in l1:
  for j in l2:
    if i==j:
      inter.append(i)
print(uni)
print(inter)
print(l1 and l2)
print(l1 or l2)