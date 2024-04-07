def main():
    frac = input('Fraction: ' )
    percent = convert(frac)
    status = gauge(percent)
    print(status)

#raises error and convert to percentage
def convert(fraction):
    while True:
        try:
            num , den = fraction.split('/')
            num1 = int(num)
            num2 = int(den)
            if num2 == 0:
                raise ZeroDivisionError

            elif num1 < num2 or num1 == num2:
                return round((num1 / num2) * 100)
            
            else:
                raise ValueError

        except ValueError:
            raise


def gauge(percentage):
    if percentage <= 1:
        return 'E'

    elif percentage >= 99:
        return 'F'

    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
