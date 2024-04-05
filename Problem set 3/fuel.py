while True:
    try:
        num , den = input('Fraction: ').split('/')
        num1 = int(num)
        num2 = int(den)
        if num1 > num2:
            continue
        else:
            ans = round((num1 / num2) * 100)

            if ans <= 1:
                print('E')

            elif ans >= 99:
                print('F')

            else:
                print(f'{ans}%')

            break

    except (ValueError, ZeroDivisionError):
        continue
