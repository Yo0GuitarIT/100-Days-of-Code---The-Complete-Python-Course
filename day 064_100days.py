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
	subject = None
	position = None
	
	def __init__(self,name,salary,hoursWork,subject,position):
		self.name = name
		self.salary = salary
		self.hoursWork = hoursWork
		self.subject = subject
		self.position = position
		
	def data(self):
		print(f"Job type: {self.name}")
		print(f"Salary: $ {self.salary}")
		print(f"Hours worked: {self.hoursWork}")
		print(f"Subject: {self.subject}")
		print(f"Position: {self.position}\n")

class doctor(job):
	speciality = None
	YearsOfExperience = None

	def __init__(self,name,salary,hoursWork,speciality,YearsOfExperience):
		self.name = name
		self.salary = salary
		self.hoursWork = hoursWork
		self.speciality = speciality
		self.YearsOfExperience = YearsOfExperience

	def data(self):
		print(f"Job type: {self.name}")
		print(f"Salary: $ {self.salary}")
		print(f"Hours worked: {self.hoursWork}")
		print(f"Speciality: {self.speciality}")
		print(f"Years of Experience: {self.YearsOfExperience}")
		
print("Jobs Jobs Jobs!\n")
p1 = job("Lawyer","Squillions",60)
p1.data()

p2 = teacher("Teacher","Nowhere near enough","All of them","Computer Science","Classroom Teacher")
p2.data()

p3 = doctor("Doctor","Doing very nicely thank you",50,"Pediatric Consultant",7)
p3.data()
