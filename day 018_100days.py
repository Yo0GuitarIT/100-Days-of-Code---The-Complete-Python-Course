from getpass import getpass as input

print("E P I C 😉 B A T T L E")
print("Select your own move(r, p or s)")

counter = 0
P1_score = 0
P2_score = 0

while True:
	print("Player1's score =>",P1_score,"Player2's score=>",P2_score)

	if counter < 3:
		#game
		P1 = input("Player 1=")
		P2 = input("Player 2=")
		
		if P1 == "r":
			if P2 =="r":
				print("Even\n")
			elif P2 =="p":
				print("Player2's papper is win to Playe1's rock\n")
				P2_score += 1
				counter+=1
			elif P2 =="s":
				print("Player1's rock is win to Playe2's scissor\n")
				P1_score += 1
				counter+=1
			else:
				print("Player2 Please enter correct ans.\n")
		
		elif P1 =="p":
			if P2 =="r":
				print("Player1'paper is win to Playe2'rock\n")
				P1_score += 1
				counter+=1
			elif P2 =="p":
				print("Even\n")	
			elif P2 =="s":
				print("Player2's scissor is win to Player1's papper\n")
				P2_score += 1
				counter+=1
			else: 
				print("Player2 Please enter correct ans.\n")
		
		elif P1 =="s":
			if P2=="r":
				print("Player2's rock is win to Player1's scissor\n")
				P2_score += 1
				counter+=1
			elif P2 =="p":
				print("Player1's scissor is win to Player2's papper\n")
				P1_score += 1
				counter+=1
			elif P2 =="s":
				print("Even\n")		
			else:
				print("Player2 Please enter correct ans.\n")
				
		else:
			print("Player1 Please enter correct ans.\n")
		continue
	else:
		break
print("Tahnk you , Game is over")
exit()
