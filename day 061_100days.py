from replit import db
import datetime, time, os
rec = {}


def recTime():
	timestamp = datetime.datetime.now()
	year = str(timestamp.year)
	month = str(timestamp.month)
	day = str(timestamp.day)
	hour = str(timestamp.hour)
	min = str(timestamp.minute)
	sec = str(timestamp.second)
	return year+month+day+hour+min+sec

def add():
	item = input("T@> ")
	timer = recTime()
	rec[counter]= timer
	db[timer] = item
	

def view():
	clr = 0
	for i in range(counter-1,-1,-1):
		key = rec[i]
		value = db[key]
		print(value)
		time.sleep(0.5)
		clr+=1
		if clr == 10:
			os.system("clear")

counter = 0
while True:
	print("Tweeter")
	print("1. Add Tweets")
	print("2. View Tweets")
	option = int(input(">"))
	os.system("clear")
	if option == 1:
		add()
		counter+=1
	else:
		view()

