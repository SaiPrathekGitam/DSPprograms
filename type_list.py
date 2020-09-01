l = list()
for i in range(int(input('Enter Length Of List : '))):
    l.append(input())

for i in l:
    try:
        int(i)
        print(i, '- Integer')
    except:
        try:
            float(i)
            print(i, '- Float')
        except:
            print(i, '- String')