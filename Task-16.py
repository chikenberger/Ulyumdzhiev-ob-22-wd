class Cat:
    def __init__(self, name, age, colour):
        self.name   = name
        self.age    = age
        self.colour = colour

    def getCatInfo(self):
        print(f"{self.name}, {self.age} лет, цвет {self.colour}")

