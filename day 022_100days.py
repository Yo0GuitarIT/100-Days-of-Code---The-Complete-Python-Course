import random

num = random.randint(1, 1000000)

counter = 0
#print(num)

print("Totally Random One-Million-to-One")
while True:
	i = int(input("What is your guess?:"))
	if i ==  num:
		print("Correct")
		break
	elif i > num:
		print("too high")
		counter+=1
	else:
		print("too low")
		counter+=1
print("It took you", counter ,"guesses to get the number correct.Click 'run' to try again with a different number.")
