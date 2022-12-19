import random,os,time
while True:
	os.system("clear")
	print("IDEAS")
	print("""
1: Add an idea
2: Load up a random idea
	""")
	
	ans = int(input(">"))
	if ans == 1:
		os.system("clear")
		print("IDEAS\n")
		f = open("my.ideas","a+")
		Text = input("Idea > ")
		f.write(f"{Text}\n")
		f.close()
	elif ans ==2:
		os.system("clear")
		print("IDEAS\n")
		f = open("my.ideas","r")
		idea = f.read().split("\n")
		f.close()
		print("Random idea: ",random.choice(idea))
		time.sleep(2)
	else:
		print("Please try again~")
		time.sleep(1)
		os.system("clear")
		
