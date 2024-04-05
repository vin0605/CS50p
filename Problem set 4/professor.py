import random


def main():
    n = get_level()
    score = 0

    #Ten questions
    for _ in range(10):

        x , y = generate_integer(n)
        z = x + y

        #Three chances
        for i in range(3):
            try:
                ans = int(input(f'{x} + {y} = '))

                if ans == z:
                    score += 1
                    break

                elif ans != z:
                    if i == 0 or i == 1:
                        print('EEE')
                        continue

                    elif i == 2:
                        print(f'{x} + {y} = {z}')

            except ValueError:
                if i == 0 or i == 1:
                        print('EEE')
                        continue

                elif i == 2:
                    print(f'{x} + {y} = {z}')



    print(f'Score: {score}')



def get_level():
    while True:
        try:
            lvl = int(input('Level: '))
            if lvl in [1,2,3]:
                return lvl
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
                if level == 2 or level == 3:
                    min_value = 10 ** (level - 1)
                    max_value = (10 ** level) - 1
                    x_value = random.randint(min_value, max_value)
                    y_value = random.randint(min_value, max_value)
                    return x_value, y_value
                elif level == 1:
                    min_value2 = 0
                    max_value2 = 9
                    x_value2 = random.randint(min_value2, max_value2)
                    y_value2 = random.randint(min_value2, max_value2)
                    return x_value2, y_value2


if __name__ == "__main__":
    main()
