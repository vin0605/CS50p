def main():
    string = input('Input: ')
    new_string = shorten(string)
    print(f'Output: {new_string}')

def shorten(x):
    strng = ''
    for char in x:
        if char not in ['a','e','i','o','u','A','E','I','O','U']:
            strng += char
    return strng

if __name__ == "__main__":
    main()
