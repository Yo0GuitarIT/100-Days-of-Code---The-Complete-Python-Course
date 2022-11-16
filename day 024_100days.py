import random

print("Infinity Dice 🎲")

num = int(input("How many dice?:"))

def RollDice(num):
	roll = random.randint(1, num)
	print("You rolled",roll,"\n")

RollDice(num)

while True:
	ans = input("Roll again? Y/n\n")
	if ans =="Y" or ans =="y":
		RollDice(num)
	elif ans =="N" or ans == "n":
		exit()
	else:
		print("try agan\n")
