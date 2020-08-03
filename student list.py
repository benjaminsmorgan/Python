IDs = { 's001' : {'fname' : 'John', 'lname' : 'Doe', 'grade' : '09', 'email' : 'john.doe@school.edu'},
        's002' : {'fname' : 'Jane', 'lname' : 'Rex', 'grade' : '12', 'email' : 'jane.rex@school.edu'},
        's003' : {'fname' : 'Andrew', 'lname' : 'Jerk', 'grade' : '01', 'email' : 'andrew.jerk@school.edu'}}
a = input("Enter the student ID#:")
x = IDs.items()
IDs["fname"] = a
print(x)
#print(IDs[a])
#print(a)
#b = next((sub for sub in IDs if sub['is'] == a), None)
#print(str(b))
#class student:
#    def __init__(self, fname, lname, grade, email):
#        self.id = id
#        self.fname = fname
#        self.lname = lname
#        self.grade = grade
#        self.email = email
#s001 = student("s001", "John", "Doe", "12", "John.Doe@school.edu")
#s002 = student("s002" "Jane", "Johnson", "09", "Jane.Johnson@school.edu")
#a = input("Select Student ID: ")
#print(a.fname)
    