#class bcolors:
#    OK = '\033[92m' #GREEN
#    WARNING = '\033[93m' #YELLOW
#    FAIL = '\033[91m' #RED
#    RESET = '\033[0m' #RESET COLOR

#print(bcolors.OK + "File Saved Successfully!" + bcolors.RESET)
#print(bcolors.WARNING + "Warning: Are you sure you want to continue?" + bcolors.RESET)
#print(bcolors.FAIL + "Unable to delete record." + bcolors.RESET)

import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)