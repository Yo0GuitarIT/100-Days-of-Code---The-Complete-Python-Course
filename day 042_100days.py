print("MokéBeast - The Non-Copyright Generic Beast Battle Game\n")

mokebeast = {"Beast name":None, "Type":None, "Special move":None, "Hp":None,"Mp":None}

for i in mokebeast.keys():
	mokebeast[i] = input(f"Input your beast's {i} > ").title()

if mokebeast['Type'] == "Fire":
			print("\033[1;31m",end="") #red
elif mokebeast['Type'] == "Water":
			print("\033[1;34m",end="") #blue
elif mokebeast['Type'] == "Earth":
			print("\033[1;33m",end="") #brown
elif mokebeast['Type'] == "Air":
			print("\033[1;36m",end="") #Cyan
elif mokebeast['Type'] == "Spirit":
			print("\033[1;35m",end="") #purple

for m,n in mokebeast.items():
	print(f"{m:<15}: {n}")
