import time

# def say_hello(func):
#     def wrapper():
#         print('Привет!')
#         func()
#         print('Пока!')
#     return wrapper

# @say_hello
# def just_func():
#     print('Как дела?')

# just_func()

# ##############

# def add_logs(func):
#     def wrapper(*args):
#         print(f'Вызывается {func.__name__} с аргументами {args}')
#         result = func(*args)
#         print(f'Функция {func.__name__} завершила работу')
#         return result
#     return wrapper

# @add_logs
# def add(a, b):
#     return a + b

# print(add(3, 2))

####################################################

def time_decorator(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f'Время выполнения функции {func.__name__}: {end_time - start_time} секунд')
        return result
    return wrapper


@time_decorator
def add(a, b):
    time.sleep(0.5)
    return a + b

add(3, 2)