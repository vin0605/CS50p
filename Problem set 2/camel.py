def main():
    cc = input("camelCase: ")
    print(snake(cc), end = '')

def snake(lol):
    sc = ''
    for char in lol:
        if char.isupper():
            sc += '_' + char.lower()
        else:
            sc += char

    return sc

main()