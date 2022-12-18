import random,os

mycharater = {}
Comcharater = {}

charater = []
Mr_Speck            = {"Intelligence":100,"Handsomeness":40,"L33t c0ding skillz":60,"Baldness level":80}
David               = {"Intelligence":80,"Handsomeness":100,"L33t c0ding skillz":40,"Baldness level":60}
Monica_from_Friends = {"Intelligence":60,"Handsomeness":80,"L33t c0ding skillz":100,"Baldness level":40}
Professor_X         = {"Intelligence":40,"Handsomeness":60,"L33t c0ding skillz":80,"Baldness level":100}
card = {"Mr Speck":Mr_Speck,"David":David,"Monica from Friends":Monica_from_Friends,"Professor X":Professor_X}

for i in card:
	charater.append(i)

def choosecharater(num):
	print(f"{charater[num-1]} is be choosen\n")
	if num == 1:	
		return Mr_Speck
	elif num == 2:
		return David
	elif num == 3:
	  return  Monica_from_Friends
	elif num == 4:
		return Professor_X

def stat(id,num):	
	if num == 1:
		return id["Intelligence"]
	elif num == 2:
		return id["Handsomeness"]
	elif num == 3:
		return id["L33t c0ding skillz"]
	elif num == 4:
		return id["Baldness level"]

def battle(myValue,comValue):
	print()
	if myValue > comValue:
		print(f"{charater[3]} is winner\n")
	else:
		print(f"{com} is winner\n")
while True:	
	print("Top Trumps\n")
	print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator\n")
	print("""Choose your card: 
	1 - Mr Speck  
	2 - David
	3 - Monica from Friends
	4 - Professor X\n""")
	
	print("Choose your charator:")
	num = int(input("> "))
	mycharater = choosecharater(num)
	
	plus = charater[num-1]
	charater.remove(charater[num-1])
	print("Computer has picked:")
	com = random.choice(charater)
	charater.append(plus)
	
	if com in card.keys():
		print(com)
		Comcharater = card[com]
	
	print("""\nChoose your stat:
	1. Intelligence
	2. Handsomeness
	3. L33t c0ding skillz
	4. Baldness level\n""")
	
	Stnum = int(input(">"))
	myValue = stat(mycharater,Stnum)
	comValue = stat(Comcharater,Stnum)
	print()
	print(f"{charater[3]}: {myValue}")
	print(f"{com}: {comValue}")
	
	battle(myValue,comValue)
	
	ans = input("Again? y/n:").lower()
	if ans == "y":
		os.system("clear")
	else:
		break
