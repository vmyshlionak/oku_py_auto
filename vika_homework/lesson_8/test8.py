from vika_homework.lesson_8.utils import helper


def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

# for number in progression(10):
#     print(number)
# print(list(progression(10)))

count = 1
for number in progression(1000000000000000000000000):
    if count == 9:
        print(number)
        break
    count += 1

print(list(progression(15)))

print(helper.variable)

helper.assist()


