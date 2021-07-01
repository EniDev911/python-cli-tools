
import bcrypt

def generate_password():
	pass_text = input("Registra tu contraseña: ")
	pass_text = pass_text.encode()
	sal = bcrypt.gensalt()
	pass_secure = bcrypt.hashpw(pass_text, sal)
	return pass_secure

def main():
	passw_user = generate_password()

	passw_input = input("Ingresa tu contraseña: ")
	passw_input = passw_input.encode()


	if bcrypt.checkpw(passw_input, passw_user):
		print("Bienvenido a tu cuenta")
		return
	print("Correo y/o contraseña incorrectos")


if __name__  == "__main__":
	main()

