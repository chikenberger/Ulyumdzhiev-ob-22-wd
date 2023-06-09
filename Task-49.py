class ProductCard:
    def __init__(self, name, cost, quantity):
        self._name = name
        self._cost = max(0, cost)
        self._quantity = max(0, quantity)

    def decrease_quantity(self, amount):
        if amount >= 0 and amount <= self._quantity:
            self._quantity -= amount
            print(f"Количество товара '{self._name}' уменьшено на {amount}")
        else:
            print("Ошибка: некорректное количество для уменьшения")

    def change_cost(self, new_cost):
        if new_cost >= 0:
            self._cost = new_cost
            print(f"Стоимость товара '{self._name}' изменена на {new_cost}")
        else:
            print("Ошибка: некорректная стоимость")

    def display_info(self):
        print("Карточка товара:")
        print(f"Название: {self._name}")
        print(f"Стоимость: {self._cost}")
        print(f"Количество: {self._quantity}")



product = ProductCard("Монитор", 5000, 10)
product.display_info()

product.decrease_quantity(5)
product.display_info()

product.change_cost(4500)
product.display_info()

product.decrease_quantity(10)
product.change_cost(-2000)
