def main():
    lmao = input('Greeting: ').strip()
    money = value(lmao)
    print(f'${money}')

def value(greeting):
    char = greeting[0]
    if 'hello' in greeting.lower():
        return 0
    elif "h" in char.lower():
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
