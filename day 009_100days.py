
while True:
	year = int(input("What generation are you a part of? "))
	if year >= 1925 and year <=1946 :
	  print("Traditionalists")
	elif year >= 1947 and year <= 1964:
	  print("Baby Boomers")
	elif year >= 1965 and year <= 1981:
	  print("Generation X")
	elif year >= 1982 and year <= 1995:
	  print("Millenials")
	elif year >= 1996:
	  print("Generation Z")	
	else:
		print("Try again.")
