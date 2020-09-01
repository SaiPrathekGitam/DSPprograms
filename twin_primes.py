# Program to print twin primes upto specified limit

def prime(num):
    if num==4:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input('Enter The Lower Limit : '))
m = int(input('Enter The Upper Limit : '))
for i in range(n, m):
    if prime(i) and prime(i+2):
        print(i, i+2)
