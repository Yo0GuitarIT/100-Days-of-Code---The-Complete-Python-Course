import time
print("HIGH SCORE TABLE")
while True:
	f = open("high.score","a+")
	initial = input("Input your initials > ")
	score = input("Input your score > ")
	f.write(f"{initial} {score}\n")
	time.sleep(1)
	f.close()
	print("\nAdded to high score table.")
	ans = input("Add another? y/n?\n").lower()
	if ans == "n":
		break
