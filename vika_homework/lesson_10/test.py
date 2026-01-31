def outer():

    def inner():
        result = 5 + 2
        return result

    return inner

new_inner = outer()
print(new_inner())
#OR
print(outer()())

#decorators

#функция-декоратор, которая должна принимать в качестве аргумента другие функции, которые мы хотим "декорировать"

def add_text(func):
    def wrapper(a, b):
        print(a)
        func()
        print(b)

    return wrapper

#декорируем другую функцию враппером
@add_text
def simple_function():
    print('inside simple_function')

simple_function('before','after')

####################################################
#Пример декоратора для логирования работы функций

def add_logs(func):
    def wrapper(*args):
        print(f'function {func.__name__} started')
        result = func(*args)
        print(f'finished {func.__name__}')
        return result

    return wrapper


@add_logs
def simple1():
    print('simple1')


@add_logs
def print_nothing():
    return 'hello'


@add_logs
def calc(x):
    print(x * 2)


@add_logs
def calc2(x, y):
    print(x * y)


simple1()
print(print_nothing())
calc(3)
calc2(3, 7)

#LIST COMPREHENTION

my_list = [1, 2, 3]

new_list = [x * 3 for x in my_list] # замена функции map+lambda, проходящей по списку и совершающей с элементами операции)
print(new_list)

#словари

data = [('one', 'two'), ('three', 'four')]

#корявый вариант
# new_dict = {}
# for key, value in data:
#     new_dict[key] = value

#менее корявый вариант
#new_dict = {key: value for key, value in data}

#норм вариант (но это если у нас список из парных кортежей)
new_dict = dict(data)

print(new_dict)

#вариант, когда есть два списка, которые надо в словарь совместить - через функцию zip

countries = ['USA', 'Hawaii', 'Cuba']
temps = [23, 33, 35]

country_temps_dict = dict(zip(countries, temps))
print(country_temps_dict)