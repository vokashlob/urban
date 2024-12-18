import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()



def initiate_db():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    );
    ''')


def add_product(id, title, description, price):
    cursor.execute(f'INSERT INTO Products VALUES("{id}", "{title}", "{description}", "{price}")')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products


def add_user(username, email, age):
    counter = cursor.execute('SELECT COUNT(*) FROM Users').fetchone()
    cursor.execute(f'INSERT INTO Users VALUES("{int(counter[0]) + 1}", "{username}", "{email}", "{age}", "1000")')
    connection.commit()


def is_included(username):
    test = cursor.execute(f'SELECT username FROM Users WHERE username = "{username}"').fetchone()
    connection.commit()
    return True if test else False

# add_product(1, 'Постельное белье 2 спальное Веселина, Бербари, бязь, наволочки 50х70, 100% хлопок',
#             'Постельное белье двуспальное с евро простыней от бренда Веселина ассоциируется только с уютом, '
#             'комфортом и практичностью.', 1294)
# add_product(2, 'Гирлянда Нить 10 м мультиколор диоды 80 шт, 8 режимов, зеленый провод, 220-240В, '
#                'IP20 контроллер', 'Гирлянда «Твинкл» длиной 10 метров с 80 светодиодами — это эффектное '
#                                   'интерьерное украшение, которое создаст неповторимую атмосферу праздника в вашем '
#                                   'доме.', 586)
# add_product(3, 'Держатель для Алисы Лайт 2, подставка колонки Яндекс станции light2 в розетку, черный',
#             'Держатель для Яндекс Станции Лайт 2 в чёрном цвете — уникальная 3D-модель, специально созданная'
#             'для вашей умной колонки Алисы и напечатанная на 3D-принтере из прочного пластика с выраженным рельефом и'
#             'слоями. Этот держатель позволяет компактно разместить Яндекс Станцию под полкой или на стене, освобождая'
#             'пространство в доме или на кухне.', 544)
# add_product(4, 'Набор бокалов для пива из 6-ти штук объемом 415мл', 'Вы ищете идеальный подарок для'
#             'пивного гурмана? Представляем вам наш набор бокалов для пива - идеальное сочетание стиля, функциональности '
#             'и удовольствия от этого неподдельно мужского напитка. Наш подарочный набор станет украшением для любого'
#             'стола и прекрасным дополнением к вашей коллекции посуды. Высокие стеклянные бокалы придают особый шарм'
#             'пиву.', 935)

# print(get_all_products())
# initiate_db()
# add_user('test', 'e@mail.com', 25)
# print(is_included('test'))
# print(is_included('sdfgsdfg'))
# cursor.execute('DROP TABLE Users')

connection.commit()
