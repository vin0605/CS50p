def main():
    txt = input()
    conv(txt)

def conv(text):
    print(text.replace(":)","🙂").replace(":(","🙁"))

main()