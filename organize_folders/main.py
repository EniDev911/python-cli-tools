import organize 
import time
import os 

USER_PATH = os.getenv('userprofile')
USERNAME = os.getenv('username')

folders = {"Desktop": "[1].DESKTOP", 
		   	"Documents": "[2].DOCUMENTS", 
		    "Downloads": "[3].DOWNLOADS"}

	
list_folders_keys = list(folders.keys())
list_folders_values = list(folders.values())


def clear_screen():
	platform = os.name 
	if platform == 'posix':
		os.system('clear')
	elif platform == 'nt' or platform == 'ce' or platform == 'dos':
		os.system('cls')

def get_folder():

	while True:

		clear_screen()
		print('USER : {}'.format(USERNAME.upper()).center(40))
		print("SELECT THE FOLDER TO ORGANIZE:".center(40))
		print("------------------------------".center(40)+"\n")
		print(list_folders_values[0], end="")
		print(list_folders_values[1].rjust(14), end="")
		print(list_folders_values[2].rjust(14), end="\n\n")
		print("[4].EXIT".center(40))
		print("------".center(40)+"\n")
		print()

		try:
			choice = input("(CHOICE): ".rjust(24))
			if int(choice) == 1:
				return os.path.join(USER_PATH, list_folders_keys[0])

			elif int(choice) == 2:
				return os.path.join(USER_PATH, list_folders_keys[1])

			elif int(choice) == 3:
				return os.path.join(USER_PATH, list_folders_keys[2])

			elif int(choice) == 4:
				break

		except ValueError:
			print("YOU MUST ENTER [1,2,3 or 4]".rjust(30))
			print('\a')
			print("+".rjust(7)+"--"*9+"+")
			print("|  OPTION INVALID!".rjust(24)+'|'.rjust(2))
			print("+".rjust(7)+"--"*9+"+")
			time.sleep(1)
			clear_screen()
			get_folder()


def main():

	while True:
		clear_screen()
		print(":=="*15+":")
		print("|\tWELCOME TO FILE ORGANIZER"+'|'.rjust(13))
		print(":=="*15+":")
		print("CHOOSE AN OPTION:".center(40))
		print("-----------------".center(40)+"\n")
		print("[O]RGANIZER FILES".rjust(20), end="")
		print("[E]XIT THE PROGRAM".rjust(20)+"\n")


		try:
			opt = input("(CHOICE): ".rjust(24))

			if opt.upper() == 'O':
				
				folder = get_folder()

				if folder != None:
					clear_screen()
					organize.organizer(folder)
					time.sleep(2)

			elif opt.upper() == 'E':
				
				print("+".rjust(5)+"--"*16+"+")
				print("| THANKS FOR USING THIS PROGRAM".rjust(35)+"|".rjust(3))
				print("|".rjust(5)+"DEVELOPED BY ENIDEV911".rjust(27)+"|".rjust(6))
				print("+".rjust(5)+"--"*16+"+")
				time.sleep(2)
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
	main()