import os,time

try:
	f = open("inventory.txt","r")
	list = eval(f.read())
	f.close()
except Exception as err:
	print("ERROR: Unable to load")
	print(err)
	time.sleep(3)
	os.system("clear")

list = ["Sword"]
RPG = {}

def Add():
	item = input("Item to add > ").capitalize()
	list.append(item)
	time.sleep(0.5)
	print("done")
	time.sleep(0.5)
	
def View():
	RPG.clear()
	for item in list:
		if item not in RPG:
			num = list.count(item)
			RPG[item] = num
	time.sleep(1)
	for key,value in RPG.items():
		print(f"{key}:{value}")
	enter = input("Press enter to continue")
	os.system("clear")

def Remove():
	item = input("Item to remove > ").capitalize()
	if item in list:
		list.remove(item)
	time.sleep(0.5)
	print("done")
	time.sleep(0.5)

while True:
	print("inventory".upper())
	print("=========")
	print("""
1.Add
2.View
3.Remove
	""")
	action = int(input(">"))
	time.sleep(0.5)
	os.system("clear")
	if action == 1:
		Add()
	elif action == 2:
		View()
	elif action ==3:
		Remove()
	else:
		print("Please try again~")
	f = open("inventory.txt", "w")
	f.write(f"{str(list)}")
	f.close()
