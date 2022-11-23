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
	
def CharacterBuilder():
	time.sleep(0.5)
	name = input("Name Your Legend:")
	type = input("Character Type (Human, Elf, Wiard, Orc):")
	print()
	time.sleep(0.5)
	print(name)
	hp = health()
	str = strength()
	print("HEALTH:",hp)
	print("STRENGTH:",str)
	print()
	time.sleep(0.5)
	return name,hp,str


print("⚔️ BATTLE TIME ⚔️")
p1,hp1,str1 = CharacterBuilder()
print("Who are they battling?\n")
p2,hp2,str2 = CharacterBuilder()
time.sleep(0.5)
os.system("clear")

print("⚔️ BATTLE TIME ⚔️\n")
print("The battle begins!")
while True:
	dicep1 = DiceRoll(6)
	dicep2 = DiceRoll(6)
	if dicep1 > dicep2:
		attack = p1
		damage = p2
		hp2-=8
		break
	elif dicep1 < dicep2:
		attack = p2
		damage = p1
		hp1-=8
		break
	else:
		continue

print(attack,"wins the first blow",damage,"takes a hit, with 8 damage\n")
print(p1)
print("HEALTH:",hp1)
print()
print(p2)
print("HEALTH:",hp2)
print()
print("And they're both standing for the next round!\n")
time.sleep(2)
os.system("clear")

counter = 2
while True:
	print("⚔️ BATTLE TIME ⚔️\n")
	print("The battle continues!")
	while True:
		dicep1 = DiceRoll(6)
		dicep2 = DiceRoll(6)
		if dicep1 > dicep2:
			attack = p1
			damage = p2
			hp2-=8
			break
		elif dicep1 < dicep2:
			attack = p2
			damage = p1
			hp1-=8
			break
		else:
			continue
	
	print(attack,"wins round",counter)
	print(damage,"takes a hit, with 8 damage\n")
	print(p1)
	print("HEALTH:",hp1)
	print()
	print(p2)
	print("HEALTH:",hp2)
	counter +=1
	time.sleep(0.5)
	if hp1 <=0:
		alive = p2
		died = p1
		break
	elif hp2 <=0:
		alive = p1
		died = p2
		break
	else:
		print("And they're both standing for the next round!\n")
		time.sleep(1)
		os.system("clear")
		
time.sleep(1)		
os.system("clear")
print()
print("Oh no",died,"the Mighty has died!")
print(alive,"the Almighty destroyed Arthur the Magnificent in",counter,"rounds!")
