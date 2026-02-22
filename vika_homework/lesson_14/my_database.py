import mysql.connector as mysql

# Твои настройки для XAMPP
# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',  # в XAпше PP по умолчанию пусто
#     'database': 'my_autotest_db'
# }

# try:
#     # Пытаемся подключиться
#     with mysql.connect(**config) as conn:
#         if conn.is_connected():
#             print("✅ Успех! PyCharm видит базу 'my_autotest_db'")
#
#             # Проверим, что таблицы на месте
#             cursor = conn.cursor()
#             cursor.execute("SHOW TABLES")
#             tables = cursor.fetchall()
#
#             print(f"Таблицы в базе: {tables}")
#
# except mysql.connector.Error as err:
#     print(f"❌ Ошибка подключения: {err}")


db = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='my_autotest_db'
)

cursor = db.cursor(dictionary=True)

# cursor.execute('select * from Students')
#
# # ШАГ 2: Выгружаем данные из курсора в переменную
# data = cursor.fetchall()
#
# # ШАГ 3: Печатаем результат
# for student in data:
#     print(student['last_name'])


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

# тройные кавычки позволяют разбивать запрос по строкам для красоты и читаемости
query = '''
            SELECT Books.title AS book_name, Students.first_name, Students.last_name
            FROM Books
            LEFT JOIN Students ON Books.taken_by_student_id = Students.id
        '''

cursor.execute(query)
results = cursor.fetchall()

print(f"{'КНИГА':<20} | {'КТО ВЗЯЛ':<20}")
print("-" * 45)

for row in results:
    # Если книга никем не взята, в имени будет None
    student_name = f"{row['first_name']} {row['last_name']}" if row['first_name'] else "В библиотеке"
    print(f"{row['book_name']:<20} | {student_name:<20}")

insert_query = '''
Insert into Students (first_name, last_name, group_id)
VALUES (%s, %s, %s)
'''

data2 = [('Ivan', 'Ivanov', 1), ('Petr', 'Petrov', 1)]
cursor.executemany(insert_query, data2)

cursor.execute("select * from students order by id desc limit 1")
print(cursor.fetchone())

db.commit()



