import os,time
list = []

def myprint():
	os.system("clear")
	print("To do List:")
	for i in range(len(list)):
		print(f"{i+1}: {list[i]}" )
		
while True:
	print("To Do List Manager:")
	step = input("Do you want to view, add, edit, or remove an item from the to do list?\n")
	if step == "view":
		myprint()
		time.sleep(1)
		os.system("clear")
	elif step == "add":
		item = input("What do you want to add?\n")
		list.append(item)
		print("Done.")
		time.sleep(0.5)
		os.system("clear")
	elif step == "edit":
		item = input("What do you want to edit?\n")
		if item in list:
			new_item = input(f"Change {item} to?\n")
			for j in range(len(list)):
				if item == list[j]:
					list[j] = new_item
		else:
			print(f"{item}","was not in the list")
		print("Done")
		time.sleep(0.5)
		os.system("clear")
	elif step == "remove":
		item = input("What do you want to remove?\n")
		if item in list:
			print(f"Are you sure to remove {item} ?")
			ans = input("Y/n?\n")
			if ans == "Y" or ans == "y":
				list.remove(item)
				print("it has be removed.")
			else:
				print("please try again.")
		else:
			print(f"{item}","was not in the list")
		time.sleep(0.5)
		os.system("clear")
	else:
		print("Please try again~~~")
		os.system("clear")
