import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', 10 * i, 1000))


cursor.execute('UPDATE Users SET balance = ? WHERE ID % 2 = 1', (500,))

cursor.execute('DELETE FROM Users WHERE ID % 3 = 1')

cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Возраст: {user[2]} | Почта: {user[3]} | Баланс: {user[4]}')

# cursor.execute('DROP TABLE Users')

connection.commit()
connection.close()
