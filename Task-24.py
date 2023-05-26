class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def presentation(self):
        print("Имя: ", self.name)
        print("Возраст: ", self.age)
        print("Зарплата: ", self.salary)

employee = Employee("Иван", 30, 50000)

employee.presentation()
