# Accept a number and print it's odd digits
num = int(input('Enter The Number : '))
print('The Odd Numbers In The Given Number Are :')
for i in str(num):
    if int(i) % 2 != 0:
        print(i, end=' ')
