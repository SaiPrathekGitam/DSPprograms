# Print type of input
i = input('Enter The Value : ')
try:
    print(int(i), '- Integer')
except:
    try:
        print(float(i), '- Float')
    except:
        print(i, '-String')
