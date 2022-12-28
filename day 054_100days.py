import csv 

with open("Day54Totals.csv") as file:
	reader = csv.DictReader(file)
	total = 0
	for row in reader:
		spend = float(row["Cost"])*float(row["Quantity"])
		total += spend
	print(f"You shop took {round(total,2)}")
