import random 
import time

print("Welcome to Rolling Dice Simulator")

choice = input("Want to roll the dice? (y/n): ")

while(choice.lower()=='y'):
	
	print('throwing the dice...')
	
	time.sleep(2)
	num = random.randint(1,6)	
	
	if num == 1:
		print("+---------+")
		print("|         |")
		print("|","0".center(7),"|")
		print("|         |")
		print("|         |")
		print("+---------+")
	
	elif num == 2:
		print("+---------+")
		print("|         |")
		print("|","0 0".center(7),"|")
		print("|         |")
		print("|         |")
		print("+---------+")
		
	elif num == 3:
		print("+---------+")
		print("|         |")
		print("|","0 0 0".center(7),"|")
		print("|         |")
		print("|         |")
		print("+---------+")
	
 
	elif num == 4:
		print("+---------+")
		print("|         |")
		print("|","0 0 0 ".center(7),"|")
		print("|","0".center(7),"|")
		print("|         |")
		print("+---------+")
	
	elif num == 5:
		print("+---------+")
		print("|         |")
		print("|","0 0 0".center(7),"|")
		print("|","0 0".center(7),"|")
		print("|         |")
		print("+---------+")
		
	else:
		print("+---------+")
		print("|         |")
		print("|","0 0 0".center(7),"|")
		print("|","0 0 0".center(7),"|")
		print("|         |")
		print("+---------+")
	
	choice = input("Want to roll the dice? (y/n): ")
	
	
	if choice=='n':
		exit()
