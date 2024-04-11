'''
demo file:

#zaza

name = 'bob'
print(name)
'''

import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

else:
    if sys.argv[1][-3:] != '.py':
        sys.exit('Not a Python file')

    else:

        try:
            file = open(sys.argv[1], 'r')

            lines = file.readlines()
            #readline and readlines have a difference
            '''
            print(lines)
            results in,
            ['#zaza\n', '\n', "name = 'bob'\n", 'print(name)']
            readlines takes the newline literally as \n
            '''

            n = 0
            for line in lines:
                if line.strip() == '':
                #cant do if line == '' or line == '\n'
                # cuz an empty line is not empty string as it has whitespace
                #it may also be a couple spaces in the newline
                    continue
                if line.strip().startswith('#') == True:
                #cant do if line.startswith('#') cuz it could be space space #comment
                #cant do if '#' in line as the code may have # somewhere in the middle but its not meant to be a comment
                    continue
                else:
                    n += 1


            print(n)



        except FileNotFoundError:
            sys.exit('File does not exist')


'''
                print(line)
                results in:
                '
                #zaza



                name = 'bob'

                print(name)
                '
                print function has a default end = '\n'
                and the \n in list will work as well, hence:

                #zaza \n due to zaza
                \n due to print
                \n due to '\n'
                \n due to print
                name = 'bob'
'''
