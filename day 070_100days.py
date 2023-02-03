import os

while True:
	print("Login System\n")
	key = input("Uername > ")
	password = os.environ[key] 
	userPass = input("Password > ")
	if key == "admin":
		if userPass == password:
			print("Hello admin")
			break
		else:
			print("Sorry, Please try again.")
	elif key =="normal":
		if userPass == password:
			print("Hello normie")
			break
		else:
			print("Sorry, Please try again.")
	else:
		print("Good luck for next time.")
