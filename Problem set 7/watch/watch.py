import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s):
        #shouldnt add ^ or/and $ as our re isnt starting form the begining or ending at the end
        # r'^.+src="https?://(?:www\.)?youtube\.com/embed/(\w+)".+$'
        return 'https://youtu.be/' + matches.group(1)


if __name__ == "__main__":
    main()
