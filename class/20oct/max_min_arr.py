# 4.Find the maximum and minimum element in an array
l =  list(map(int, input('Enter List Elements : ').split()))
m1 = l[0]
m2 = l[0]
for i in l:
  if m1>i:
    m1=i
  if m2<i:
    m2=i
print('Max : ', m2, 'Min : ', m1)