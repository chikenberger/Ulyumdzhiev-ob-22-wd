class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def getPersonInfo(self):
        print(vars(self))

