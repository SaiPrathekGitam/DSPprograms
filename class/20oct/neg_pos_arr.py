# 7.  Move all the negative elements to one side of the array 
l =  list(map(int, input('Enter List Elements : ').split()))
temp1 = []
temp2 = []
for i in l:
  if i<0:
    temp1.append(i)
  else:
    temp2.append(i)
print('Final Array', temp1+temp2)