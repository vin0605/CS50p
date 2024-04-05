string = input('Input: ')

for char in string:
    if char in ['a','e','i','o','u','A','E','I','O','U']:
        print('', end = '')
    else:
        print(char, end = '')
