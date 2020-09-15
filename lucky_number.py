# Accept date of birth and calculate the lucky number
nums = ''.join(input('Enter Your DOB(DD-MM-YYYY) : ').split('-'))
while True:
    s = 0
    for i in nums:
        s += int(i)
    if s < 10:
        break
    nums = str(s)

print('Your Lucky Number Is', s)
