print("""MY LOGIN SYSTEM
+++++++++++++++""")
Name = input("Username > ")
Password = input("Password > ") 


if Name == "Tom":
	if Password == "111":
		print("Welcome~~")
	else:
		print("Please try again.")

elif Name == "Andy":
	if Password == "222":
		print("Welcome~~")
	else:
		print("Please try again.")

elif Name == "Jack":
	if Password == "333":
		print("Welcome~~")
	else:
		print("Please try again.")
		
else:
	print("No User")	
