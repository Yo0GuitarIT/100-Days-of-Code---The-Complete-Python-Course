import random,time,os
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords).lower()
testword = list(wordChosen)
answord = []
unknow="_"
counter = 5
#print(wordChosen)

def sumword():
	result = ""
	for w in range(len(answord)):
		result += answord[w]
	return result

letter = input("Choose a letter: ")
if letter in testword:
	print("got it!!\n")
	for i in testword:
		if i == letter:
			answord.append(i)	
		else:
			answord.append(unknow)
else:
	print("Come on~ Try again~\n")
	for i in testword:
		answord.append(unknow)
	counter-=1
print(sumword(),"\n")
print("You have",counter,"chance~\n")
time.sleep(1)
os.system("clear")

while True:
	new_letter = input("Choose a letter: ")
	if new_letter in testword:
		print("got it!!\n")
		for j in range(len(testword)):
			if new_letter == testword[j]:	
				answord[j] = new_letter
	else:
		print("come on try again~\n")
		counter -=1
		
	final = sumword()
	if final == wordChosen:
		print("You win!!")
		break
		
	if counter == 0:
		print("sorry game is over Q^Q")
		break
	else:
	 print(sumword())
	 print("You have",counter,"chance~\n")
	 time.sleep(1)
	 os.system("clear")
