import random, os, time, datetime
from replit import db

nextstep = False

def add():
	os.system("clear")
	userName = input("Username > ")
	passWord = input("Password > ")
	salt = random.randint(1000,9999)
	newPassWord = f"{passWord}{salt}"
	newPassWord = hash(newPassWord)
	db[userName] = {"Password": newPassWord,"salt":salt}
	print("It's be signed up")
	time.sleep(1)
	
def login():
	global nextstep
	os.system("clear")
	ansUserName = input("Username > ")
	ansPassWord = input("Password > ")
	keys = db.keys()
	for key in keys:
		if key == ansUserName:
			salt = db[ansUserName]["salt"]
			ansPassWord = f"{ansPassWord}{salt}"
			ansPassWord = hash(ansPassWord)
			if ansPassWord == db[key]["Password"]:
				print("Login Successful")
				nextstep = True
				time.sleep(1)
			else:
				print("Password is error.")
				time.sleep(1)
		else:
			print("Username could not be found.")
			time.sleep(1)

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break

while True:
	os.system("clear")
	print("Login System")
	step = int(input("1.Add User, 2.Login > "))
	if step == 1:
		add()
	elif step == 2:
		login()
		if nextstep:
			exit()
	else:
		print("Please try again.")

print("~~~~~~~~~~~Login~~~~~~~~~~~~~~~")
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
