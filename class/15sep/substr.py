# Accept a string and a sub-string and check whether the given substring exists in the string or not

st = input('Enter The String : ')
substr = input('Enter The Substring : ')
if substr in st:
    print(f'{substr} is present in {st}')
else:
    print(f'{substr} is not present in {st}')
