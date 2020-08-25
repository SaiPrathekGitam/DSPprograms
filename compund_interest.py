# Program to calculate compund interest

p = int(input('Enter Initial Principal Balance : '))
r = int(input('Enter ANnual Interst Rate : '))
t = int(input('Enter Time(in years) : '))
n = int(input('Enter Number Of Times Interest Applied : '))

print('Final Amount Is', p*(1+r/n)**(n*t))