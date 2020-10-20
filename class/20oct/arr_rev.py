# Question 3:  Reverse the array with using loops 
def rev(l, start, end):
  if start >= end:
      return
  l[start], l[end] = l[end], l[start]
  rev(l, start+1, end-1)