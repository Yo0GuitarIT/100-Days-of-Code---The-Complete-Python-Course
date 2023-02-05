import random
from replit import db

def add():
	userName = input("Username>")
	passWord = input("Password>")
	salt = random.randint(1000,9999)
	newPassWord = f"{passWord}{salt}"
	newPassWord = hash(newPassWord)
	db[userName] = {"Password": newPassWord,"salt":salt}
	print("It's be signed up\n")
	
def login():
	ansUserName = input("Username>")
	ansPassWord = input("Password>")
	salt = db[ansUserName]["salt"]
	newAns = f"{ansPassWord}{salt}"
	newAns = hash(newAns)

	if newAns == db[ansUserName]["Password"]:
		print("Login successful\n")

	
while True:	
	print("Login System")
	step = int(input("1.Add User, 2.Login > "))
	if step == 1:
		add()
	elif step == 2:
		login()
	else:
		print("Please try again.\n")
