name = input("Input your name > ").capitalize()
birth = input("\nInput your date of birth >")
phone_number = input("\nInput your telephone number > ")
email = input("\nInput your email > ")
address = input("\nInput your address > ")

Contact = {"name": name, "birth": birth, "phone_number":phone_number, "email":email, "address":address}

print(f"Hi {Contact['name']}. Our dictionary says that you were born on {Contact['birth']}, we can call you on {Contact['phone_number']}, email {Contact['email']}, or write to {['address']}")
