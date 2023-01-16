from replit import db
import datetime,os,time


def add():
	time.sleep(1)
	os.system("clear")
	timestamp = datetime.datetime.now()
	print(f"Diary entry for {timestamp}")
	print()
	entry = input("> ")
	db[timestamp] = entry
	
def view():
	keys = db.keys()
	for key in keys:
		time.sleep(1)
		os.system("clear")
		print(f"""{key}  {db[key]}""")
		print()
		opt = input("Next or exit? > ")
		if(opt.lower()[0]=="e"):
			break
