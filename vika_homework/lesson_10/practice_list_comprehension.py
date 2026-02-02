from typing import Any


from collections import defaultdict

my_list = [1, 2, 3, 4, 5]

new_list = [x ** 2 for x in my_list]
print(new_list)

####################################################

mixed = [3, -1, 4, -5, 2, 0, -10]
positive_list = [x for x in mixed if x >= 0]
print(positive_list)

####################################################

new_list = [x if x > 0 else 0 for x in mixed]
print(new_list)

####################################################

new_list = [x if x > 0 else print(f'{x} is negative') for x in mixed]
print(new_list)

####################################################

words = ["яблоко", "кот", "программирование", "питон"]

new_list = [len(word) for word in words]
print(new_list)

####################################################

numbers = [1, 2, 3, 4, 5]

new_dict = {x: x ** 2 for x in numbers}

print(new_dict)

####################################################

words = ["арбуз", "банан", "апельсин", "груша"]

new_dict = {word[0]: word for word in words}

print(new_dict)

new_dict = defaultdict(list)

for word in words:
    new_dict[word[0]].append(word)

print(dict(new_dict))

####################################################

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [x * 2 if x % 2 == 0 else x for x in nums]

print(new_list)