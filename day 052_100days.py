import time,os

try:
	f = open("pizza.txt","r")
	list = eval(f.read())
	f.close()
except Exception as err:
	print("ERROR: Unable to load")
	print(err)
	time.sleep(1)
	os.system("clear")
	
list = [["Name","Topping","size","Quantity","Total"]]

def add():
	name = input("Name:\n").capitalize()
	topping = input("Topping:\n").capitalize()
	choose_size = int(input("Choose (1.Large 2.Medium 3.Small): "))
	if choose_size == 1:
		size = "Large"
		calculate = 1.5
	elif choose_size == 2:
		size = "Medium"
		calculate = 1.3
	else:
		size = "Small"
		calculate = 1.1
		
	try:
		quantity = int(input("Quantity: "))
		total = round(calculate*quantity,1)
		row = [name,topping,size,quantity,total]
		list.append(row)
		time.sleep(1)
		os.system("clear")
	except Exception as err:
		print("Wrong Input! Please try again.")
		print(err)
		time.sleep(1)
		os.system("clear")
		
def view():
	for item in list:
		print(f"{item[0]:^15}{item[1]:^15}{item[2]:^15}{item[3]:^15}{item[4]:^15}")
		time.sleep(0.5)
		os.system("clear")
		
while True:
	print("Dave's Dodgy Pizza")
	print("""
1.add Pizzas
2.view Pizzas
	""")
	move = int(input(">"))
	if move == 1:
		add()
	elif move == 2:
		view()
	else:
		print("Please try again")
		
	f = open("pizza.txt", "w")
	f.write(f"{str(list)}")
	f.close()
