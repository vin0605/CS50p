import random

while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            n = []
            for i in range(level):
                n.append(i+1)

            break

        else:
            continue

    except ValueError:
        continue

number = random.choice(n)

while True:


    try:
        guess = int(input('Guess: '))
        if guess == number:
            print('Just right!')
            break

        elif guess < number:
            print('Too small!')
            continue

        elif guess > number:
            print('Too large!')
            continue
    except ValueError:
        continue
