import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        num_list = ip.split('.')
        for number in num_list:
            if int(number) > 255 or int(number) < 0:
                return False
            else:
                continue
        return True
    else:
        return False

if __name__ == "__main__":
    main()
