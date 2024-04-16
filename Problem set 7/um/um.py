import re

def main():
    print(count(input("Text: ")))


def count(s):
    matches =  re.findall(r"\bum\b", s, re.IGNORECASE)
    #cant use := as it'll return none instead of 0 when the case isnt true
    return len(matches)



if __name__ == "__main__":
    main()
