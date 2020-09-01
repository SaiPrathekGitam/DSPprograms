# Program to accept a number and verify whether it is a number or not

x = int(input('Enter A Number : '))

try:
    x=int(x)
    print('The Number Is', x)
except:
    print('The Given Input', x, 'Is Not A Number')
finally:
    print('End Of The Program.')
