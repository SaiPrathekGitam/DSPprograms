# Question 2. write a program to find the reverse of a given number without any loops.

# print(input('Enter A Number : ')[::-1])

rnum = 0
pos = 1
def rev(num):
  global rnum
  global pos
  if(num > 0): 
      rev(num // 10)
      rnum += (num % 10) * pos 
      pos *= 10
  return rnum
print(rev(int(input('Enter The Number'))))
