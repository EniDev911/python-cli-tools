
#import os
#import shutil

#a = shutil.get_terminal_size((40, 20))  # pass fallback
#a = shutil.get_terminal_size((80, 20))  # pass fallback
#print(a)
#os.terminal_size(columns=37, lines=10)  # returns a named-Tuple

#print(os.terminal_size())


import os
os.system('mode con: cols=10 lines=2')

input("Pantalla: ")
# XTERM
#import os
#os.system('printf "\033[8;10;42t"')