print("Factorial Finder")


def function(value):
	if value == 1:
		return 1
	else:
		total = value*function(value-1)
		return total

num = int(input("Input a number > "))
ans = function(num)
print(f"The factorial of {num} is {ans}.")
