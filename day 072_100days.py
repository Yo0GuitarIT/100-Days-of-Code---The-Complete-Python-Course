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
	salt = db[ansUserName]["salt"]
	newAns = f"{ansPassWord}{salt}"
	newAns = hash(newAns)
	if newAns == db[ansUserName]["Password"]:
		print("Login successful")
		nextstep = True
	else:
		print("Login Error")
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
  keys = db.keys()
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
			break
	else:
		print("Please try again.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)
nextstep = False

while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n 3:Log out\n>")
  if menu == "1":
    addEntry()
  elif menu == "2":
    viewEntry()
  else:
    print("Log out")
    break
