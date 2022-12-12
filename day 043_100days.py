import random;

num = [None,None,None,None,None,None,None,None,None]
addCard = [[None,None,None],[None,None,None],[None,None,None]]

a = 0
while True:
	if a == 9:
		break
	randNum = random.randint(0,90)
	for k in num:
		if randNum == k:
			None
		else:
			num[a] = randNum
	a+=1	

num.sort()
t=0
for i in range(3):
	for j in range(3):
		addCard[i][j] = num[t]
		t+=1

addCard[1][1] = "BINGO"

print("David's Nan's Bingo Card Genrator")
print(f"{addCard[0][0]:^8} | {addCard[0][1]:^8} | {addCard[0][2]:^8}" )	
print("-----------------------------")
print(f"{addCard[1][0]:^8} | {addCard[1][1]:^8} | {addCard[1][2]:^8}" )	
print("-----------------------------")
print(f"{addCard[2][0]:^8} | {addCard[2][1]:^8} | {addCard[2][2]:^8}" )	
