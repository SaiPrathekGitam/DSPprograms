# Write a program to accept a number and print it's individual digit sum
# try:
#     num = int(input('Enter The Number : '))
#     s = 0
#     temp = num
#     for i in str(num):
#         s+=int(i)
#     print(f'Individual Digits Sum Of {temp} is {s}')
# except:
#     print('Enter A Valid Input.')

# Print type of input
# i = input('Enter The Value : ')
# try:
#     print(int(i), '- Integer')
# except:
#     try:
#         print(float(i), '- Float')
#     except:
#         print(i, '-String')

# Program to generate and catch value, index, name and general exceptions

# try:
#     num = input()
#     x = int(num)
#     print('abc'+x)
#     # print(x)
#     l = [1, 2, 3]
#     # print(l[4])
#     print(123/0)
# except TypeError:
#     print('The Error is TypeError')
# except ValueError:
#     print('The Error is ValueError')
# except NameError:
#     print('The Error is NameError')
# except IndexError:
#     print('The Error is IndexError')
# except Exception:
#     print('The Error is General Exception')