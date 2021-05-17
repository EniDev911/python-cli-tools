import crud 
import connection as conn

db = conn.Database()

def main():
	while True:
		print(":=="*20)
		print("\t\tCONSOLE CRUD WITH SQLITE3")
		print(":=="*20)
		print("[C]REATE NEW DATABASE")
		print("[D]ROP DATABASE")
		print("[U]SE DATABASE")
		print("[E]xit")
		print(":=="*20)

		try:
			opt = input('Select one option:\n')

			if opt.upper() == 'C':
				crud.clear()
				db.createDB()
			elif opt.upper() == 'D':
				db.dropDB()

			elif opt.upper() == 'U':
				while True:
					print("[1] Insert a row")
					print("[2] Show all row")
					print("[3] Update a row")
					print("[4] Delete a row")
					print("[5] Search a row")
					print("[6] Exit")
					print(":=="*20)
					try:
						option = int(input('Select a option:\n'))

						if option == 1:
							crud.clear()
							crud.create()
						if option == 2:
							crud.clear()
							crud.get()
						if option == 3:
							crud.update()
						elif option  == 4:
							crud.delete()
						elif option == 6:
							crud.clear()
							break
					except:
						print('Option invalid!')	

			elif opt.upper() == 'E':
				break
		except:
			print('Option invalid!')

if __name__ == '__main__':
	main()