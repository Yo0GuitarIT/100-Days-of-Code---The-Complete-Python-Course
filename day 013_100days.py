print("Exam Grade Calculator")

name = input("Name of exam:")
max_score = int(input("Max. Possible Score:"))
score = int(input("Your Score:"))

final = float(score/max_score)
final_number = round(final,2)	
perc = round(final*100,2)

print("You got",perc,"%")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")
