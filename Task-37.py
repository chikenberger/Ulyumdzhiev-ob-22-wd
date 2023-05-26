def find_two_smallest(numbers):
    smallest1 = float('inf')
    smallest2 = float('inf')

    for num in numbers:
        if num < smallest1:
            smallest2 = smallest1
            smallest1 = num
        elif num < smallest2:
            smallest2 = num

    return smallest1, smallest2

numbers = input("Введите список чисел через пробел: ").split()
numbers = [int(num) for num in numbers]

smallest1, smallest2 = find_two_smallest(numbers)

print("Два наименьших значения в списке:")
print(smallest1)
print(smallest2)
