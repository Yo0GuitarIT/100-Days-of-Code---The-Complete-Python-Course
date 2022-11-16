artist = input("What is your favorite artist? \nAimer or Hyde :")
if artist == "Aimer":
  print("Nice")
  album = input("Which album is the best? ")
  if album == "Good Day":
    print("Right answer")
  else:
    print("Nah, 'Good Day' is the best")
elif artist == "Hyde":
	print("Rock guy")
	album = input("Which album is the best? ")
else:
  print("OK...Fine...")
