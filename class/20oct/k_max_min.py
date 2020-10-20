# 5.  Find the "Kth" max and min element of an array
l =  list(map(int, input('Enter List Elements : ').split()))
k = int(input())
m1 = l[0]
m2 = l[0]
for i in range(len(l)-1):
  m = i
  for j in range(i+1, len(l)):
    if l[m] < l[j]:
      m = j
  l[i], l[m] = l[m], l[i]
print('Max : ', l[k-1], 'Min : ', l[-k])