# Create a list of n numbers and perfor tasks
n = [1, 1, 2, 3, 1, 2, 4, 4]
# a. print the count of elements/items in the list
print('The count of elements/items in the list is ', len(n))
# b. print the max. item of the list
print('The Max item of the list is', max(n))
# c. print the min. item of the list
print('The Min item of the list is', min(n))
# d. print the count of each element in the list if items are duplictes
print('The count each of elements in the list is : ')
for i in set(n):
    if n.count(i) > 1:
        print(f'{i} is repeated for for {n.count(i)} times')
    else:
        print(f'{i} is not repeated')
