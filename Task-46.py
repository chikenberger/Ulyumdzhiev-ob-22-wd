try:
    with open("test.txt", "w") as file:
        file.write("Hello, world!")
        print("Запись выполнена успешно")

except IOError:
    print("Ошибка: Ошибка при записи файла")
