def rfact(n):
    if n<2:
        return 1
    return n*rfact(n-1)


def fact(n):
    f = 1
    for i in range(1, n+1):
        f*=i
    return f

num = int(input('Enter A Positive Integer : '))
print(fact(num))
print(rfact(num))
factorial = 1
while(num>1):
    factorial*=num
    num-=1
print(factorial)

# wap to accept a sentence and toggle the case