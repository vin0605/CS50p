def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    test1 = s[:2]
    for char3 in test1:
        if char3.isalpha():
            continue
        if char3.isdigit():
            return False




    length = len(s)
    if length < 2:
        return False
    if length > 6:
        return False



    punc = ['.', ',', ':', '#']
    for char4 in s:
        if char4 in punc:
            return False




    string = ''
    for char in s:
        if char.isalpha():
            continue

        if char.isdigit():
            string = s[s.index(char):]
            break

    if string and string[0] == '0':
        return False

    for char2 in string:
        if char2.isdigit():
            continue
        if char2.isalpha():
            return False

    else:
        return True



main()
