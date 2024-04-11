import sys
import csv
from tabulate import tabulate

list = []

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

else:
    if sys.argv[1][-4:] != '.csv':
        sys.exit('Not a CSV file')

    else:

        try:
            with open(sys.argv[1]) as file:
                pizza, small, large = file.readline().strip().split(',')

            with open(sys.argv[1]) as file2:
                reader = csv.DictReader(file2)

                for row in reader:
                    list.append({f'{pizza}':row[f'{pizza}'], f'{small}':row[f'{small}'], f'{large}': row[f'{large}']})

            print(tabulate(list, headers='keys', tablefmt="grid"))
        except FileNotFoundError:
            sys.exit('File does not exist')
