class job:
	name = None
	salary = None
	hoursWork = None
	
	def __init__(self,name,salary,hoursWork):
		self.name = name
		self.salary = salary
		self.hoursWork = hoursWork

	def data(self):	
		print(f"Job type: {self.name}")
		print(f"Salary: $ {self.salary}")
		print(f"Hours worked: {self.hoursWork}\n")
	
class teacher(job):
	
	def __init__(self):
		self.name = "Teacher"
		self.salary = "Nowhere near enough"
		self.hoursWork = "All of them"
		self.subject = "Computer Science"
		self.position = "Classroom Teacher"
		
	def data(self):
		print(f"Job type: {self.name}")
		print(f"Salary: $ {self.salary}")
		print(f"Hours worked: {self.hoursWork}")
		print(f"Subject: {self.subject}")
		print(f"Position: {self.position}\n")

class doctor(job):

	def __init__(self):
		self.name = "Doctor"
		self.salary = "Doing very nicely thank you"
		self.hoursWork = 50
		self.speciality = "Pediatric Consultant"
		self.YearsOfExperience = 7

	def data(self):
		print(f"Job type: {self.name}")
		print(f"Salary: $ {self.salary}")
		print(f"Hours worked: {self.hoursWork}")
		print(f"Speciality: {self.speciality}")
		print(f"Years of Experience: {self.YearsOfExperience}")
		
print("Jobs Jobs Jobs!\n")
p1 = job("Lawyer","Squillions",60)
p1.data()

p2 = teacher()
p2.data()

p3 = doctor()
p3.data()
