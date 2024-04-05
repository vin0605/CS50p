'''
def main():

    due  = 50

    print('Amount Due:', due)

    while True:

        newdue = calcdue(due)

        if newdue > 0:
            print('Amount Due:', newdue)
            calcdue(newdue)

        else: #newdue < 0

            print('Change Owned:', newdue * -1)
            break





def calcdue(lol):

    while lol > 0:
        inserted = int(input('Insert Coin: '))

        if inserted == 25 or inserted == 10 or inserted == 5:

            lol -= inserted

            return lol

        else:

            continue


main()
'''

def main():

    due = 50
    print('Amount Due:', due)

    while due > 0:
        inserted = int(input('Insert Coin: '))

        if inserted in [25,10,5]:

            due -= inserted

            if due > 0:
                print('Amount Due:', due)

            else:
                print("Change Owed:", due * -1)

        else:
            print('Amount Due:', due)
            continue

main()
