import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('students.db')

# Создание курсора для выполнения запросов
cursor = conn.cursor()

# Создание таблицы "students" с полями "name", "age" и "average_score"
cursor.execute('''
    CREATE TABLE students (
        name TEXT,
        age INTEGER,
        average_score REAL
    )
''')

# Вставка данных о студентах в таблицу "students"
students = [
    ('Иванов', 20, 4.5),
    ('Петров', 19, 3.8),
    ('Сидоров', 21, 4.2)
]

cursor.executemany('''
    INSERT INTO students (name, age, average_score)
    VALUES (?, ?, ?)
''', students)

# Выполнение запроса на выборку всех данных из таблицы "students" и вывод на экран
cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()

for student in all_students:
    print(student)

# Закрытие курсора и соединения с базой данных
cursor.close()
conn.close()