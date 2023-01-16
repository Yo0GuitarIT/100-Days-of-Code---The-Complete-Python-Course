import rec,os

passWord = input("Password:")
if passWord != "123":
	print("Incorrect")
	exit()
else:
	while True:
		os.system("clear")
		print("1.Add 2.view")
		move = int(input(">"))
		if move == 1:
			rec.add()
		else:
			rec.view()
