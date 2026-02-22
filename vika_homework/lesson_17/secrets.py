from vika_homework.lesson_17 import creds
import mysql.connector as mysql

db = mysql.connect(
    host=creds.host,
    user=creds.user,
    password=creds.password,
    database=creds.database
)

cursor = db.cursor(dictionary=True)

cursor.execute('select * from Students')

# ШАГ 2: Выгружаем данные из курсора в переменную
data = cursor.fetchall()

# ШАГ 3: Печатаем результат
for student in data:
    print(student['last_name'])
