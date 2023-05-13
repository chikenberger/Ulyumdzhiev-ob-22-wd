class Student:
    def __init__(self, firstName, lastName, course):
        self.firstName = firstName
        self.lastName = lastName
        self.course = course

    def getStudentInfo(self):
        print(vars(self))

