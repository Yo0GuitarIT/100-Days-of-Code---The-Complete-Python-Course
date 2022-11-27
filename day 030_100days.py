print("30 Days Down\n")
for i in range(1,30):
	thought = input(f"Day{i}:\n")
	print()
	myText = f"You thoght Day {i} was"
	print(f"{myText:^35}")
	print(f"{thought:^35}")
	print()
