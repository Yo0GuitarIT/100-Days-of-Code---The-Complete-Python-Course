print("How many seconds are in a year?")
year = int(input("which year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

if year%4 == 0:
	sec = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute
	print("Total is",sec)
else:
	sec = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
	print("Total is",sec)
