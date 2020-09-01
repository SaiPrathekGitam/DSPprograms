# Program to print prime numbers upto specified limit

def prime(num):
    if num==4:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input('Enter The Lower Limit : '))
m = int(input('Enter The Upper Limit : '))
for i in range(n, m+1):
    if prime(i):
        print(i, end =' ')