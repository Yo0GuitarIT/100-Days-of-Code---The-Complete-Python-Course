import os,time

fname = []
lname = []

def mylist():
	for i in range(len(fname)):
		print(f"{fname[i]} {lname[i]}")

while True:
	os.system("clear")
	print("Name List")
	firstname = input("First name:").strip().capitalize()	
	lastname = input("Last name:").strip().capitalize()
	if firstname in fname and lastname in lname:
		print("Input Duplication")
		time.sleep(1)
		mylist()
		
	else:
		fname.append(firstname)
		lname.append(lastname)
	os.system("clear")
	
	mylist()
	time.sleep(1)
