import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('books.db')

# Создание курсора для выполнения запросов
cursor = conn.cursor()

# Создание таблицы "books" с полями "title" (название), "author" (автор) и "year" (год выпуска)
cursor.execute('''
    CREATE TABLE books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Вставка данных о книгах в таблицу "books"
books = [
    ('Book 1', 'Author 1', 1998),
    ('Book 2', 'Author 2', 2005),
    ('Book 3', 'Author 3', 2002),
    ('Book 4', 'Author 4', 2010),
    ('Book 5', 'Author 5', 1999),
    ('Book 6', 'Author 6', 2012),
]

cursor.executemany('''
    INSERT INTO books (title, author, year)
    VALUES (?, ?, ?)
''', books)

# Выполнение запроса на выборку всех книг, выпущенных после 2000 года, и вывод на экран
cursor.execute('SELECT * FROM books WHERE year > 2000')
recent_books = cursor.fetchall()

for book in recent_books:
    print(book)

# Закрытие курсора и соединения с базой данных
cursor.close()
conn.close()
