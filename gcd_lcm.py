# Program to find gcd and lcm of given numbers

n, m = int(input("Enter First Number : ")), int(input("Enter Second Number : "))
h = 1
for i in range(2, n):
    if n % i == m % i == 0:
        h = i

print(f"GCD of {n} and {m} is {h} and LCM  is {(n*m)//h}")
