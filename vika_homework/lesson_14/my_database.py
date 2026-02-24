import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD', ''), # '' — значение по умолчанию, если пароля нет
    'database': os.getenv('DB_NAME'),
    'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': True
}

# try:
#     # Все, что внутри try, имеет 4 пробела от края
#     with pymysql.connect(**config) as conn:
#         with conn.cursor() as cursor:
#             cursor.execute("SHOW TABLES")
#             print(cursor.fetchall())
#
# # Блок except должен быть СТРОГО под словом try (0 пробелов отступа друг от друга)
# except pymysql.MySQLError as err:
#     print("❌ Ошибка подключения")  # Теперь здесь не будет ошибки


# try:
#     # Шаг 1: Подключаемся
#     with pymysql.connect(**config) as db:
#         with db.cursor() as cursor:
#             # Шаг 2: Выполняем запрос
#             cursor.execute('SELECT * FROM Students')
#
#             # Шаг 3: Выгружаем данные
#             data = cursor.fetchall()
#
#             # Шаг 4: Печатаем результат (теперь это словари!)
#             for student in data:
#                 print(student['last_name'])
#
# except pymysql.MySQLError as err:
#     print(f"❌ Ошибка базы данных: {err}")

# db = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='my_autotest_db'
# )

#мой дешманский код вместо красивого вверху (с with и try-except):

db = pymysql.connect(**config)
cursor = db.cursor()

cursor.execute('select * from Students')

# ШАГ 2: Выгружаем данные из курсора в переменную
data = cursor.fetchall()

# ШАГ 3: Печатаем результат
for student in data:
    print(student['last_name'])
#
#
# # query = "select * from Students WHERE first_name = '{0}' and last_name = '{1}'" уязвимый для sql-инъекций код
# # 1. Запрос пишем со специальными плейсхолдерами %s
# query = "SELECT * FROM Students WHERE first_name = %s AND last_name = %s"
#
# # 2. Получаем данные от пользователя
# f_name = input('Введите имя: ').strip()   # .strip() уберет лишние пробелы
# l_name = input('Введите фамилию: ').strip()
#
# # 3. Передаем данные вторым аргументом в execute (в виде кортежа)
# cursor.execute(query, (f_name, l_name))
#
# data = cursor.fetchall()
#
# if not data:
#     print("Пользователь не найден")
# else:
#     print(data)
#
# #тройные кавычки позволяют разбивать запрос по строкам для красоты и читаемости
# query = '''
#             SELECT Books.title AS book_name, Students.first_name, Students.last_name
#             FROM Books
#             LEFT JOIN Students ON Books.taken_by_student_id = Students.id
#         '''
#
# cursor.execute(query)
# results = cursor.fetchall()
#
# print(f"{'КНИГА':<20} | {'КТО ВЗЯЛ':<20}")
# print("-" * 45)
#
# for row in results:
#     # Если книга никем не взята, в имени будет None
#     student_name = f"{row['first_name']} {row['last_name']}" if row['first_name'] else "В библиотеке"
#     print(f"{row['book_name']:<20} | {student_name:<20}")
#
# insert_query = '''
# Insert into Students (first_name, last_name, group_id)
# VALUES (%s, %s, %s)
# '''
#
# data2 = [('Sidor', 'Sidorov', 1), ('Jan', 'Moucha', 1)]
# cursor.executemany(insert_query, data2)
#
# cursor.execute("select * from students order by id desc limit 1")
# print(cursor.fetchone())
#
# db.commit()
db.close()