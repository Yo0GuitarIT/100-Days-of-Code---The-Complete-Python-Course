import os,time
list = []

def myprint():
	print()
	for item in list:
		print(item)
	print()
	
while True:
	print("To Do List Manager")
	do = input("Do you want to view, add , or edit your to do list?\n")
	if do =="view":
		myprint()
		time.sleep(1)
	elif do =="add":
		item = input("What do you want to add?\n")
		list.append(item)
		time.sleep(1)
	elif do =="edit":
		ans = input("remove? Y/n\n")
		if ans == "Y" or ans == "y":
			item = input("What do you want to remove?\n")
			if item in list:
				list.remove(item)
			else:
				print(f"{item}","was not in the list")
				time.sleep(1)
		elif ans == "N" or ans == "n":
			print("try again~")
			time.sleep(1)
	else:
		print("Please try again~")	

	time.sleep(1)
	os.system("clear") 
