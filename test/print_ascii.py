import os

def print_option():

	print(" ____") 
	print("||c ||")
	print("||__|| [C]reate")
	print("|/__\\|")

	print(" ____".rjust(9)) 
	print("||s ||".rjust(10))
	print("||__|| ".rjust(11), "[S]how")
	print("|/__\\|".rjust(10))

	print(" ____".rjust(9)) 
	print("||e ||".rjust(10))
	print("||__|| ".rjust(11), "[E]dit")
	print("|/__\\|".rjust(10))

	print(" ____".rjust(9)) 
	print("||d ||".rjust(10))
	print("||__|| ".rjust(11), "[D]elete")
	print("|/__\\|".rjust(10))

def print_option2():
	print(
		""" 
 ____                           ____ 
||c ||                         ||s ||
||__|| [C]reate                ||__|| [S]how
|/__\\|                         |/__\\|

    ____                 ____            
   ||e ||               ||d ||
   ||__|| [E]dit        ||__|| [D]elete
   |/__\\|               |/__\\|
            
               ____ 
              ||q ||
              ||__|| [Q]uit
              |/__\\|

   """)

	#print(" ____".rjust(9)) 
	#print("||s ||".rjust(10))
	#print("||__|| ".rjust(11), "[S]how")
	#print("|/__\\|".rjust(10))

	#print(" ____".rjust(9)) 
	#print("||e ||".rjust(10))
	#print("||__|| ".rjust(11), "[E]dit")
	#print("|/__\\|".rjust(10))

	#print(" ____".rjust(9)) 
	#print("||d ||".rjust(10))
	#print("||__|| ".rjust(11), "[D]elete")
	#print("|/__\\|".rjust(10))



def print_title():
	print("                 _             _ ")      
	print("                | |           | |")      
	print("  ___ ___  _ __ | |_ __ _  ___| |_ ___") 
	print(" / __/ _ \\| '_ \\| __/ _` |/ __| __/ __|")
	print("| (_| (_) | | | | || (_| | (__| |_\\__ \\")
	print(" \\___\\___/|_| |_|\\__\\__,_|\\___|\\__|___/")
                                        



def print_author():
	print(" ______         _  _____                 ___  __  __") 
	print("|  ____|       (_)|  __ \\               / _ \\/_ |/_ |")
	print("| |__    _ __   _ | |  | |  ___ __   __| (_) || | | |")
	print("|  __|  | '_ \\ | || |  | | / _ \\\\ \\ / / \\__, || | | |")
	print("| |____ | | | || || |__| ||  __/ \\ V /    / / | | | |")
	print("|______||_| |_||_||_____/  \\___|  \\_/    /_/  |_| |_|")



os.system("mode 1000, 1000")
#print_author()
#print_title()
print_option2()
