print("🌟Website Rating🌟")

myDictionary = {"name" : None, "URL" : None, "desc" : None, "rating" : None}

for i in myDictionary.keys():
	myDictionary[i] = input(f"{i}:")

print()
for item ,value in myDictionary.items():
	print(f"{item}:{value}")
