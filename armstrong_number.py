# Program to check for armstrong number

n = input('Enter The Number : ')
s=0
l = len(n)
for i in n:
    s+=int(i)**l
if s==int(n):
    print('Armstrong Number')
else:
    print('Not An Armstrong Number')