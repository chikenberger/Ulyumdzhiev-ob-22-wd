import os

file_list = os.listdir()

print("Список файлов в текущей директории:")
for file_name in file_list:
    print(file_name)
