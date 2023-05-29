try:
    number = float(input("Введите число: "))
    square = number ** 2
    print("Квадрат числа:", square)

except ValueError:
    print("Ошибка: Некорректный ввод числа")
