# n = int(input('Enter The Number Of Rows : '))
n = 3
t = n*2-1
for i in range(n, 0, -1):
    for j in range(t):
        print(i, end = ' ')
    print()
for i in range(n):
    for j in range(n):
        print(n-i, end='')
    print()
