import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

else:
    try:
        list1 = []
        list2 = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                list1.append({'name':row['name'], 'house':row['house']})
                #make list of dicts
                '''
                list1 = [
                    {'name': 'Abbott, Hannah', 'house': 'Hufflepuff'},
                    {'name': 'Bell, Katie', 'house': 'Gryffindor'},
                    ...
                ]
                '''

            for each_dict in list1:
                names = each_dict['name']
                last, first = names.split(',')
                first = first.strip()
                #first = 'Hannah' , last = 'Abbott'

                list2.append({'first':first , 'last':last , 'house':each_dict['house']})

        field_names = ['first', 'last', 'house']

        with open(sys.argv[2], 'w', newline='') as file3:
            writer = csv.DictWriter(file3, fieldnames= field_names)
            writer.writeheader()
            writer.writerows(list2)


    except FileNotFoundError:
        sys.exit('Could not read invalid_file.csv')
