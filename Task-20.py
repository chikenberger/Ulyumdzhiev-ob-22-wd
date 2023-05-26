import random

array = []

for _ in range(10):
    random_number = random.randint(1, 100)
    array.append(random_number)

max_number = max(array)
min_number = min(array)

print("Массив:", array)
print("Максимальное число:", max_number)
print("Минимальное число:", min_number)
