import random 
import time

print("Welcome to Rolling Dice Simulator")

choice = input("Want to roll the dice? (y/n): ")

while(choice.lower()=='y'):
	
	print('throwing the dice...')
	
	time.sleep(2)
	num = random.randint(1,6)	
	
	if num == 1:
		print()
		print("+---------+".rjust(20))
		print("|         |".rjust(20))
		print("|    0    |".rjust(20))
		print("|         |".rjust(20))
		print("|         |".rjust(20))
		print("+---------+".rjust(20))
		print()


	elif num == 2:
		print()
		print("+---------+".rjust(20))
		print("|         |".rjust(20))
		print("|   0 0   |".rjust(20))
		print("|         |".rjust(20))
		print("|         |".rjust(20))
		print("+---------+".rjust(20))
		print()

	elif num == 3:
		print()
		print("+---------+".rjust(20))
		print("|         |".rjust(20))
		print("|  0 0 0  |".rjust(20))
		print("|         |".rjust(20))
		print("|         |".rjust(20))
		print("+---------+".rjust(20))
		print()
 
	elif num == 4:
		print("+---------+".rjust(20))
		print("|         |".rjust(20))
		print("|  0 0 0  |".rjust(20))
		print("|    0    |".rjust(20))
		print("|         |".rjust(20))
		print("+---------+".rjust(20))
	
	elif num == 5:
		print("+---------+")
		print("|         |")
		print("|  0 0 0  |")
		print("|   0 0   |")
		print("|         |")
		print("+---------+")
		
	else:
		print("+---------+")
		print("|         |")
		print("|  0 0 0  |")
		print("|  0 0 0  |")
		print("|         |")
		print("+---------+")
	
	choice = input("Want to roll the dice again? (y/n): ")
	
	
dialogue = 'THANKS FOR USING THIS PROGRAM'
time.sleep(1)

print('T', end='')
time.sleep(1)
print('H', end='')
time.sleep(1)


#for c in range(len(dialogue)):
#	print(dialogue[c], end="")
#	time.sleep(0.1)

exit()