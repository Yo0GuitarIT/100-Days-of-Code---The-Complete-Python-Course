def Login_system():	
	while True:
		name =input("What is your username?:")
		password = input("What is your password?:")
		
		if name == "David" and password == "baldies4life":
			print("Login in~\n")
			break
		else:
			print("Whoops! I don't recognize that username or password. Try again!\n")


print("Replit Login System")
Login_system()
print("Welcome to Replit!")
