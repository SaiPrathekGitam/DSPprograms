# Question 1:Write a program to find the max element of an array and swap it with the last unsorted value of the array.

l =  list(map(int, input('Enter List Elements : ').split()))
for i in range(len(l)-1):
  m = i
  for j in range(i+1, len(l)):
    if l[m] < l[j]:
      m = j
  l[i], l[m] = l[m], l[i]
print('Sorted Array :', l)