
import bcrypt

def generate_password():
	pass_text = input("Register a password: ")
	pass_text = pass_text.encode()
	sal = bcrypt.gensalt()
	pass_secure = bcrypt.hashpw(pass_text, sal)
	return pass_secure

def main():
	passw_user = generate_password()

	passw_input = input("Type password: ")
	passw_input = passw_input.encode()


	if bcrypt.checkpw(passw_input, passw_user):
		print("Welcome to your acount")
		return
	print("Fail password")


if __name__  == "__main__":
	main()

