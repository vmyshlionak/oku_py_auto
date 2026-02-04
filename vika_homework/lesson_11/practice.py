from abc import ABC, abstractmethod


class Group(ABC):
    pupils = True
    school_name = 42
    director = 'Marivanna'

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader


    def study(self):
        print('sit down and read')

    @abstractmethod
    def move(self):
        pass


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room

    def move(self):
        print('Run fast')


class HighGroup(Group):
    max_age = 15
    min_age = 11

    def move(self):
        print('Go slowly')

class MediumGroup(Group):
    max_age = 15
    min_age = 11


#some_group = Group('1a', 15, 'MG') #класс Group должен наследоваться от ABC, чтобы выдавать ошибки из-за некорректного обращения с его абстрактностью
#print(some_group.move()) #распечатает None, потому что метод абстрактный

first_a = PrimaryGroup('1a', 18, 'MF', 5)
first_b = PrimaryGroup('1b', 20, 'TD', 8)

eleven_a = HighGroup('11a', 22, 'AR')
#six_a = MediumGroup('6a', 25, 'RI') #не даст создать экземпляр, т.к. посчитает класс абстрактным (он тянет абстрактный метод move() из Group)

print(first_a.pupils_count)
print(first_a.class_room)
print(first_b.title)
print(first_a.title)
print(first_a.pupils)
print(first_a.building_section)
print(first_a.director)
print(first_a.max_age)
print(first_a.min_age)
print(first_a.school_name)
print(eleven_a.pupils)
# print(eleven_a.building_section)
print(eleven_a.director)
print(eleven_a.max_age)
print(eleven_a.min_age)
print(eleven_a.school_name)
first_a.study()
eleven_a.study()
first_a.move()
eleven_a.move()
#six_a.move()