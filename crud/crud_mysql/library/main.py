import time
import os 


def clear_screen():
	platform = os.name 
	if platform == 'posix':
		os.system('clear')
	elif platform == 'nt' or platform == 'ce' or platform == 'dos':
		os.system('cls')


def run_main():
	while True:
		clear_screen()
		print()
		print(":=="*15+":")
		print("|\t  CRUD-PRODUCTS-STORE"+'|'.rjust(11))
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