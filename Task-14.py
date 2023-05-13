class Student:
    def __init__(self, firstName, lastName, age, specialty):
        self.firstName  = firstName
        self.lastName   = lastName
        self.age        = age
        self.specialty  = specialty

    def getStudentInfo(self):
        print('{} - {}, {} лет, {}'.format(
            self.firstName,
            self.lastName,
            self.age,
            self.specialty
        ))
