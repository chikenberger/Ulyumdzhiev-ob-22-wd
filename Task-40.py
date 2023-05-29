import os

filename = "test.txt"

if os.path.exists(filename):
    print("Файл существует")
else:
    print("Файл не найден")
