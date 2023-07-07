import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('employees.db')

# Создание курсора для выполнения запросов
cursor = conn.cursor()

# Создание таблицы "employees" с полями "name" (имя), "position" (должность) и "salary" (зарплата)
cursor.execute('''
    CREATE TABLE employees (
        name TEXT,
        position TEXT,
        salary REAL
    )
''')

# Вставка данных о сотрудниках в таблицу "employees"
employees = [
    ('Иванов', 'Менеджер', 50000.0),
    ('Петров', 'Разработчик', 40000.0),
    ('Сидоров', 'Менеджер', 55000.0),
    ('Смирнов', 'Аналитик', 45000.0),
    ('Козлов', 'Менеджер', 60000.0),
    ('Васильев', 'Разработчик', 38000.0),
]

cursor.executemany('''
    INSERT INTO employees (name, position, salary)
    VALUES (?, ?, ?)
''', employees)

# Выполнение запроса на выборку имен сотрудников, занимающих должность менеджера, и вывод на экран
cursor.execute('SELECT name FROM employees WHERE position = "Менеджер"')
manager_names = cursor.fetchall()

for name in manager_names:
    print(name[0])

# Закрытие курсора и соединения с базой данных
cursor.close()
conn.close()
