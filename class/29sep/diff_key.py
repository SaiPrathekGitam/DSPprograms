from itertools import combinations
l = list()
for i in range(int(input('Enter Size of Array : '))):
    l.append((int(input())))
k = int(input('Enter The Key : '))
for i, j in combinations(l, 2):
    if abs(j-i) == k:
        print(i, j)