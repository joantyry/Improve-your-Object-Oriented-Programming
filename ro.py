class Students: #create a class Students.
	studentCount = 0 # this defines global name studentcount which is shsred by all instances of class Students
	def __init__ (self,name,course): # this initializes name and course of the students variables.
		self.name = name
		self.course = course
		Students.studentCount +=1 #increaments the number of students by 1

	def displayCount(self): #defines how to display the number of students
		print "Number of students = %d" % Students.studentCount
	def displayStudent(self): # defines how to display each Student
		print "Name:" ,self.name, " \n ", "Course :" ,self.course

std1 = Students ("Joan", "Maths")
std2 = Students ("Hellen", "Compscie")

setattr(std1, "course","Music")
getattr(std2, "name")
std1.displayStudent()
std2.displayStudent() 

std1.displayCount()
"#Improve"
