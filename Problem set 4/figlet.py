import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

#To get list of available fonts
figlet.getFonts()




if len(sys.argv) == 3:
    option = sys.argv[1]
    if option == '-f' or option == '--font':
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font = sys.argv[2])
            txt = input('Input: ')
            print(figlet.renderText(txt))
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

elif len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f )
    txt = input('Input: ')
    print(figlet.renderText(txt))

else:
    sys.exit('Invalid usage')

'''
print('invalid usg')
sys.exit
this has an exit status of 0

whereas
sys.exit('invalid usg')
has an exit status of 1

Exit Status 0: Indicates successful termination. This means that the program completed its execution without encountering any errors.

Non-zero Exit Status: Indicates an error or abnormal termination. Non-zero exit statuses are used to signal that the program encountered
an issue during execution. The specific non-zero value can be used to indicate different types of errors or conditions.
'''
