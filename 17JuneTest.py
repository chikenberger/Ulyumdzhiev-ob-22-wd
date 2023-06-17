"""
    Написать программу, которая принимает последовательность чисел и выводит на экран два числа:
    значение наибольшего элемента последовательности и порядковый номер этого элемента.
"""


# Функция поиска наибольшего элемента с порядковым номером
def find_max_number(numbers):
    max_number = numbers[0]
    max_index = 0

    for i, num in enumerate(numbers):
        if num > max_number:
            max_number = num
            max_index = i

    return max_number, max_index + 1

# Ввод последовательности чисел
numbers = input("Введите последовательность чисел через пробел: ").split()
numbers = [int(num) for num in numbers]

# Поиск наибольшего элемента
max_num, max_i = find_max_number(numbers)

# Вывод результата
print("Наибольший элемент:", max_num)
print("Порядковый номер:", max_i)
