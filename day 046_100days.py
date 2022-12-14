clue = {}
a = "Name"
b = "Element"
c = "Move"
d = "Hp"
e = "Mp"

def prettyPrint():
	print(f"{a:^10}|{b:^10}|{c:^10}|{d:^10}|{e:^10}")
	for i,j in clue.items():
		print(f"""{i:^10}|{j["Element"]:^10}|{j["move"]:^10}|{j["HP"]:^10}|{j["MP"]:^10}""")	
		
while True:
	print("Beast Generator")
	name = input("Input the beast name >\n").title()
	element = input("Input the beast element >\n").title()
	move = input("Input the beast special move >\n").title()
	HP = input("Input the beast starting HP >\n").title()
	MP = input("Input the beast starting MP >\n").title()
	
	clue[name] = {"Element":element, "move":move, "HP":HP, "MP":MP}
	prettyPrint()
