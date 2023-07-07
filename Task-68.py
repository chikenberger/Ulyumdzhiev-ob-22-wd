import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('movies.db')

# Создание курсора для выполнения запросов
cursor = conn.cursor()

# Создание таблицы "movies" с полями "title" (название), "genre" (жанр) и "rating" (рейтинг)
cursor.execute('''
    CREATE TABLE movies (
        title TEXT,
        genre TEXT,
        rating REAL
    )
''')

# Вставка данных о фильмах в таблицу "movies"
movies = [
    ('Фильм 1', 'Драма', 7.8),
    ('Фильм 2', 'Комедия', 6.5),
    ('Фильм 3', 'Боевик', 8.2),
    ('Фильм 4', 'Ужасы', 5.9),
    ('Фильм 5', 'Драма', 7.1),
    ('Фильм 6', 'Триллер', 6.9),
]

cursor.executemany('''
    INSERT INTO movies (title, genre, rating)
    VALUES (?, ?, ?)
''', movies)

# Ввод выбранного пользователем жанра
selected_genre = input("Введите жанр фильма: ")

# Выполнение запроса на выборку всех фильмов выбранного жанра и вывод на экран
cursor.execute('SELECT * FROM movies WHERE genre = ?', (selected_genre,))
selected_movies = cursor.fetchall()

for movie in selected_movies:
    print(movie)

# Закрытие курсора и соединения с базой данных
cursor.close()
conn.close()
