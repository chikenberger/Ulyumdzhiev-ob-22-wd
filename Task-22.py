import random

array = []

for _ in range(10):
    random_number = random.randint(1, 10)
    array.append(random_number)

sum_of_elements = sum(array)

print("Массив:", array)
print("Сумма всех элементов:", sum_of_elements)
