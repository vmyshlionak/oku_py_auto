import json

# file_data = open('data1.txt', 'r') #открываем и задаем формат (чтение)
# data = file_data.read() #вычитываем данные из файла
# data = json.loads(data) #преобразуем json в словарь
# print(data) # распечатываем содержимое
# file_data.close() # если не закрывать, то накопится критическая масса открытых файлов, но будет способ покрасивее

# более лучшее решение

# def file_read(file_name):
#     data = open(file_name, 'r')
#     data = json.load(data) # и читает, и преобразует в словарь (в отличие от loads, которая только преобразует)
#     data = data.close()
#     return data
#
# data1 = file_read('data1.txt')
# data2 = file_read('data2.txt')
#
# print(data1['Country'])
# print(data2['Country'])

# РЕШЕНИЕ С КЛАССОМ

class CountryData:

    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self._comfort = self.__is_comfort()

    def __read_file(self):
        file_data = open(self.__filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def __is_comfort(self):
        return self.__avg_temp > 25

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self._comfort

    @avg_temp.setter
    def avg_temp(self, value):
        self.__avg_temp = value

    @country.setter
    def country(self, value):
        self.__country = value

    @comfort.setter
    def comfort(self, value):
        self._comfort = value


    def __str__(self):
        return f'Your file {self.__filename} contains {self.__data}'

    def __repr__(self):
        return f'Your file {self.__filename} contains {self.__data}'

    def __add__(self, obj):
        return [self, obj]

    def __lt__(self, obj):
        return self.__avg_temp < obj.__avg_temp

    def __le__(self, obj):
        return self.__avg_temp <= obj.__avg_temp

data1 = CountryData('data1.txt')
# data1.comfort = False
# print(data1.comfort)
# # data1.data = 'skdfjhskdjf'
# print(data1.data)
# # data1.__data = {'1': 5}
# print(data1.data)
# print(data1.country)
# # print(data1.avg_temp)
data2 = CountryData('data2.txt')
# print(data2.country)
# data1.__avg_temp = 2342342
# print(data1.avg_temp)


print(data1)  # print(str(data1))
print(data1 < data2)
print(data1 <= data2)
print(data1 > data2)
print(data1 >= data2)
print(data1 + data2)