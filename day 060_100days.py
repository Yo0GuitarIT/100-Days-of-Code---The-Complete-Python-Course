import datetime

today = datetime.date.today() 

event = input("Input the event > ")
year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))

holiday = datetime.date(year,month,day) 
difference = (holiday-today).days

if today == holiday:
	print(f"{event} is today")
elif today < holiday:
	print(f"^Q^~~ {difference} days to go!")
else:
	print(f"QaQ~~ You miss it by {difference} days")
