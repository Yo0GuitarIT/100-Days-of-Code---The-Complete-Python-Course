"""
print("🌟Star Wars Name Generator🌟")

first_name = input("Input your first name > ").strip().capitalize()
last_name = input("Input your lastname > ").strip().lower()
fname = (f"{first_name[0:3]}{last_name[0:3]}")

mom_name = input("Input your mother's maiden name > ").strip().capitalize()
city = input("Input the city where you were born > ").strip().lower()
lname = (f"{mom_name[0:2]}{city[4:7]}")

print("Your Star Wars name is ",fname,lname)
"""
print("##########################")

print("🌟Star Wars Name Generator🌟")
NAME = input("Input your first name,last name,mom's name,living city:\n").split()
a=NAME[0].capitalize()
b=NAME[1].lower()
c=NAME[2].capitalize()
d=NAME[3].lower()
print(f"Your Star Wars name is {a[0:3]}{b[0:3]} {c[0:2]}{d[5:8]}")
