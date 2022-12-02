string1 = "What sentence do you want rainbow-ising?" 
string2 = "Become one with rainbow my young rainbowan"
print("\033[33m", string1)
print("\033[32m", string2)
print("\033[0m")
for letter in string2:
	if letter.lower() =="r":
		print("\033[31m",end="")
	elif letter.lower() =="b":
		print("\033[34m",end="")
	elif letter.lower() =="g":
		print("\033[32m",end="")
	elif letter.lower() =="y":
		print("\033[33m",end="")
	elif letter.lower() =="o":
		print("\033[37m",end="")
	print(letter)
	#print("\033[0m",end="")
