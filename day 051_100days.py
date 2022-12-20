import os,time
list = []

f = open("calendar.txt","r")
list = eval(f.read())
f.close()


def add():
	task = input("What is the task? > ").title()
	date = input("When is it due by? > ")
	priority = input("What is the priorty? (High/Midium/Low)>").title()
	row = [task,date,priority]
	list.append(row)

def view():
	for i in list:
		print(f"{i[0]:^8}|{i[1]:^8}|{i[2]:^8}")

def CPY():
	choosePriority = input("Which Priorty? >").title()
	for p in list:
		if choosePriority in p:
			print(f"{p[0]:^8}|{p[1]:^8}|{p[2]:^8}")

def edit():
	editItem = input("What do you edit? >").title()
	newTask = input("New title:").title()
	newDate = input("New Due Date:").title()
	newPriority = input("New Priority:").title()
	for p in list:
		if editItem in p:
			p[0] = newTask
			p[1] = newDate
			p[2] = newPriority
	
def remove():
	removeItem = input("What would you like to remove? >").title()
	for p in list:
		if removeItem in p:
			list.remove(p)

while True:
	time.sleep(1)
	os.system("clear")
	print("Life Organizer\n")
	print("Welcome to the life organizer.")
	menu = int(input(" 1:add\n 2:view\n 3:edit\n 4:remove\n"))
	if menu == 1:	#add
		add()	
	elif menu == 2:	#view
		num = int(input(" 1.View all\n 2.View priority\n"))
		if num == 1:
			view()
		elif num == 2:
			CPY()
		else:
			print("Please try again")
			
	elif menu == 3:	#edit
		edit()
		
	elif menu == 4:	#remove
		remove()
		
	else:
		print("Please Try again~")
		
	f = open("calendar.txt", "w")
	f.write(f"{str(list)}") 
	f.close()
		
