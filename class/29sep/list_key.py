l = list()
for i in range(int(input('Enter Size of Array : '))):
    l.append((int(input())))
k = int(input('Enter The Key : '))
d = int(input('Enter The Distance : '))
for i in set(l):
    if abs(k-i) == d:
        print(i)
