import os

folder_name = "my_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Директория создана: ", folder_name)
else:
    print("Директория уже существует: ", folder_name)
