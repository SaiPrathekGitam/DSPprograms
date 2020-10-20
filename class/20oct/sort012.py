#6. Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo.
l =  list(map(int, input('Enter List Elements : ').split()))
l0=[]
l1=[]
l2=[]
for i in l:
  if i ==0:
    l0.append(0)
  elif i==1:
    l1.append(1)
  else:
    l2.append(2)
print('Sorted Array : ', l0+l1+l2)
