import time,random,os

def DiceRoll(num):
	resault = random.randint(1,num)
	return resault

def health():
	healthStat = (DiceRoll(6)*DiceRoll(12))*0.5+10
	return healthStat

def strength():
	strengthStat = (DiceRoll(6)*DiceRoll(8))*0.5+12
	return strengthStat


	
	strength = (random.randint(1,6)+random.randint(1,12))*0.5+12
	return type,strength

while True:
	print("Character Builder\n")
	time.sleep(0.5)
	
	name = input("Name Your Legend:")
	type = input("Character Type (Human, Elf, Wiard, Orc):")
	print()
	time.sleep(0.5)
	print(name)
	print("HEALTH:",health())
	print("STRENGTH:",strength())
	print()
	time.sleep(0.5)
	print("May your name go down in Legend...\n")

	ans = input("again?:")
	if ans =="Yes" or ans =="yes" :
		time.sleep(1)
		os.system("clear")
	else:
		break
