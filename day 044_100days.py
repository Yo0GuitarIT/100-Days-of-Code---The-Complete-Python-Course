import random,os

num = []
Card = [[None,None,None],[None,None,None],[None,None,None]]

def ran():
		k = random.randint(1,99)
		return k

for value in range(9):
	num.append(ran())

num.sort()
t = 0
for i in range(3):
	for j in range(3):
		Card[i][j]= num[t]
		t += 1
Card[1][1] = "BINGO"

counter = 0
while True:
	print("David's Nan's Bingo Card Genrator\n")
	print(f"You got {counter} point\n")	
	
	print(f"{Card[0][0]:^8} | {Card[0][1]:^8} | {Card[0][2]:^8}" )	
	print("-----------------------------")
	print(f"{Card[1][0]:^8} | {Card[1][1]:^8} | {Card[1][2]:^8}" )	
	print("-----------------------------")
	print(f"{Card[2][0]:^8} | {Card[2][1]:^8} | {Card[2][2]:^8}\n" )

	if counter == 8:
		print("You Win~")
		break
	else:
		called = int(input("What number was called? "))
		for i in range(3):
			for j in range(3):
				if Card[i][j] == called:
					Card[i][j] = "X"
					counter += 1
		


	os.system("clear")
