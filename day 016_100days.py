print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)""")

#These days the stars seem out of reach. -->Bon Jovi

counter = 1

while True:
	word = input("These days the stars ____ out of reach.\n")
	if word == "seem":
		print("Well done! It only took you",counter,"attempt(s).")
		break
	else:
		print("Nope, try again.")
		counter +=1
