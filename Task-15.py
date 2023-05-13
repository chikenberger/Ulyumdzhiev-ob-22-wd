class Car:
    def __init__(self, brand, model, yearOfRelease, price):
        self.brand          = brand
        self.model          = model
        self.yearOfRelease  = yearOfRelease
        self.price          = price

    def getCarInfo(self):
        print('{} - {}; {}, {}'.format(
            self.brand,
            self.model,
            self.yearOfRelease,
            self.price
        ))
