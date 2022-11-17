import random

def DiceRoll(num):
	result = random.randint(1,num)
	return result

def Hp():
	A = DiceRoll(6)
	B = DiceRoll(8)
	total = A*B
	return total

print("⚔️ Character Stats Generator ⚔️")

for i in range(1,4):
	print("Name your warrior",i,":")
	warrior = input()
	print("Their health is:")
	hp = Hp()
	print(hp)
