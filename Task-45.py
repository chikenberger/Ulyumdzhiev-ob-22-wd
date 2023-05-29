try:
    filename = input("Введите имя файла для чтения: ")

    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Ошибка: Файл не найден")
except IOError:
    print("Ошибка: Ошибка при чтении файла")
