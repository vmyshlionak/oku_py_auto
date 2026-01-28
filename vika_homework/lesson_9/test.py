import datetime

my_list = [1, 2, 3, 4, 5]


def mult_by_2(x):
    return x * 2

new_list = map(mult_by_2, my_list)
print(list(new_list))

#предложила ИИ-шка

my_list = [1, 2, 3, 4, 5]

# Используем map и lambda
new_list = map(lambda x: x * 2, my_list)

print(list(new_list))

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

#FILTER - фильтрует коллекцию по каждому элементу, для которого получается True
new_list2 = filter(lambda x: x % 2 == 0, my_list2)
print(list(new_list2))

#DATETIME

easy_date = datetime.datetime(2039, 1, 15)
print(easy_date)
print(easy_date.timestamp())

#ИИ (форматы для паттерна искать здесь: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

my_time = '2023/06/05 12 hours, 30 mins, 10 secs'

# Шаблон должен в точности повторять формат строки
pattern = '%Y/%m/%d %H hours, %M mins, %S secs'

date_obj = datetime.datetime.strptime(my_time, pattern)

print(date_obj)        # 2023-06-05 12:30:10
print(type(date_obj))  # <class 'datetime.datetime'>
