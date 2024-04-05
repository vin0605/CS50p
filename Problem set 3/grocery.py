dict1 = {}

while True:
    try:
        item = input('').upper()

        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    except EOFError:
        break

sorted_dict = {key: dict1[key] for key in sorted(dict1)}

for fruit in sorted_dict:
    print(sorted_dict[fruit], fruit)
