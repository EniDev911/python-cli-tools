#-------------------------------------------------------------------------------
#         Module: main
#
#        Author: Marco Contreras
#         Email: enidev911@gmail.com
#
#   Source code: https://github.com/EniDev911/PythonTk/blob/master/audiobook/main.py
#     Copyright: (c) Marco Contreras
#       Licence: GPL 3.0
#-------------------------------------------------------------------------------
import time
import os 
from organize import USERNAME, USER_PATH, FOLDERS, organizer
from locale import getdefaultlocale 


list_folders_keys = list(FOLDERS.keys())
list_folders_values = list(FOLDERS.values())


def clear_screen():
	platform = os.name 
	if platform == 'posix':
		os.system('clear')
	elif platform == 'nt' or platform == 'ce' or platform == 'dos':
		os.system('cls')

def get_locale():
	print(getdefaultlocale())


def get_path():
	while True:
		os.system('mode con: cols=46 lines=21')
		clear_screen()
		print()
		print('USER : {}'.format(USERNAME.upper()).center(45))
		print()
		print("SELECT THE FOLDER TO ORGANIZE:".center(45))
		print("------------------------------".center(45)+"\n")
		print(" "+list_folders_values[0], end="")
		print(list_folders_values[1].rjust(16), end="")
		print(list_folders_values[2].rjust(16), end="\n\n")
		print("[4].EXIT".center(43))
		print("------".center(43)+"\n")
		print()

		try:
			choice = int(input("(CHOICE): ".rjust(24)))
			if int(choice) == 1:
				return os.path.join(USER_PATH, list_folders_keys[0])

			elif int(choice) == 2:
				return os.path.join(USER_PATH, list_folders_keys[1])

			elif int(choice) == 3:
				return os.path.join(USER_PATH, list_folders_keys[2])

			elif int(choice) == 4:
				break
			else:
				print("A ingresado una opción invalida")


		except ValueError as e:
			print("+".rjust(13)+"--"*9+"+")
			print("|  OPTION INVALID!".rjust(30)+'|'.rjust(2))
			print("+".rjust(13)+"--"*9+"+")
			print()
			print("YOU MUST ENTER [1,2,3 or 4]".rjust(36))
			print('\a')
			time.sleep(2)
			clear_screen()
			continue

def main():

	while True:
		clear_screen()
		print()
		print(":=="*15+":")
		print("|\t  WELCOME TO FILE ORGANIZER"+'|'.rjust(11))
		print(":=="*15+":")
		print("CHOOSE AN OPTION:".center(45))
		print("-----------------".center(45)+"\n")
		print("[O]RGANIZER FILES".rjust(21), end="")
		print("[E]XIT THE PROGRAM".rjust(21)+"\n")


		try:
			opt = input("(CHOICE): ".rjust(28))

			if opt.upper() == 'O':
				
				folder = get_path()

				if folder != None:
					clear_screen()
					organizer(folder) 
					time.sleep(2)

			elif opt.upper() == 'E':
				print()
				print("+".rjust(7)+"--"*16+"+")
				print("| THANKS FOR USING THIS PROGRAM".rjust(37)+"|".rjust(3))
				print("|".rjust(7)+"DEVELOPED BY ENIDEV911".rjust(27)+"|".rjust(6))
				print("+".rjust(7)+"--"*16+"+")
				time.sleep(2)
				os.system("start https://www.buymeacoffee.com/9111592")
				break

			else:
				
				print('\a')
				print("+".rjust(13)+"--"*9+"+")
				print("|  OPTION INVALID!".rjust(30)+'|'.rjust(2))
				print("+".rjust(13)+"--"*9+"+")
				time.sleep(1)

		except:
			print('\a')
			print("+".rjust(13)+"--"*9+"+")
			print("|  OPTION INVALID!".rjust(30)+'|'.rjust(2))
			print("+".rjust(13)+"--"*9+"+")
			time.sleep(1)



if __name__ == '__main__':
	os.system('mode con: cols=46 lines=19')
	os.system("color 5F")
	main()