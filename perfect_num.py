# Program to check whether the given number is perfect

n = int(input('Enter The Number : '))
l = list()
for i in range(1,n//2+1):
    if n%i==0:
        l.append(i)
print(f'{n} is Perfect') if sum(l)==n else print('{n} is Not Perfect')