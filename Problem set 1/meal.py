def main():
    masa = input("What time is it? ").strip()
    real = convert(masa)
    if 7.0 <= real <= 8.0:
        print('breakfast time')

    elif 12.0 <= real <= 13.0:
        print('lunch time')

    elif 18.0 <= real <= 19.0:
        print('dinner time')

    else:
        print()

def convert(time):
    h , m = time.split(":")
    min = float(m)
    hour = float((h))
    lolmin = min / 60
    zamin = round(lolmin , 2)
    return hour + zamin

if __name__ == "__main__":
    main()
