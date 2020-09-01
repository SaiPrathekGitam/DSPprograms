# Program to print sum of digits of a given number

n = input('Enter The Number : ')
s = 0
for i in n:
    s+=int(i)
print(f'Sum Of Digits Of {n} :', s)
