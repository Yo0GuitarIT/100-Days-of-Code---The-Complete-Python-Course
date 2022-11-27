print("Math Game!")

num = int(input("Name your multiples: "))

counter = 0

for i in range(10):
	print(i+1,"x",num,"=")
	ans =int(input())
	
	if ans == (i+1)*num:
		print("Awesome!")
		counter+=1
	else:
		print("Nope. The answer was",(i+1)*num)

if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")
