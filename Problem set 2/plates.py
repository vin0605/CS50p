def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    test1 = s[:2]
    for char1 in test1:
        if char1.isalpha():
            continue
        if char1.isdigit():
            return False




    length = len(s)
    if length < 2:
        return False
    if length > 6:
        return False



    punc = ['.', ',', ':', '#']
    for char2 in s:
        if char2 in punc:
            return False




    string = ''
    for char3 in s:
        if char3.isalpha():
            continue

        if char3.isdigit():
            string = s[s.index(char3):]
            break

    if string and string[0] == '0':
        return False

    for char4 in string:
        if char4.isdigit():
            continue
        if char4.isalpha():
            return False

    else:
        return True


if __name__ == "__main__":
    main()
