class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        distance = self.speed * time
        print(f"{self.name} прошел путь в {distance} единиц")

class TrackedRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory

class WheeledRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand

robot1 = Robot("Робот 1", 10)
robot1.movement(5)

robot2 = TrackedRobot("Гусеничный робот", 5, "Лес")
robot2.movement(3)
print(f"Территория гусеничного робота: {robot2.territory}")

robot3 = WheeledRobot("Робот на колесах", 8, "Toyota")
robot3.movement(4)
print(f"Марка автомобиля робота на колесах: {robot3.car_brand}")
