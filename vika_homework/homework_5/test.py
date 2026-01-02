my_list = [2,6]
a, b = my_list # нужно знать количество элементов списка
print(a, b)

text = 'my long long string'
print(text[4])
print(len(text))
print(text.index('long'))  # вернет индекс первого символа именно этого сочетания
print('long' in text)
print(text.count('n'))
print(text.count('long'))
print(text.find('lone'))
print(text[:7])
print(text.startswith('my'))
print(text.endswith('ng'))

txt = "ThIs tExt wiTh meSsEd uP CaPITalIZatiOn!"
print(txt.capitalize()) # Делает первую букву предложения заглавной
print(txt.title())  # Делает каждую первую букву заглавной
print(txt.upper())  # Делает все буквы большими
print(txt.lower())  # Делает все буквы маленькими


text_1 = 'mY lOng loNg STRING'
string_index = text_1.lower().index('string')
print(text_1[:string_index].lower() + text_1[string_index:].upper())

text_for_strip = '_name_'
text_for_strip = text_for_strip.strip('_')
print(text_for_strip)

languages = ['python', 'java', 'ruby']
# for language in languages:
#     print(language)

languages = ', '.join(languages).title() #достать стринги из списка, указав разделитель + сделала с заглавной
print(languages)

# Форматирование строки
a = 'one'
b = 'two'
txt_for_format = 'First word is {0}, second word is {1}'
txt_for_format = txt_for_format.format(a, b)
print(txt_for_format)

#f-string
my_text = f'First word is {{a}}, second word is {b}'
print(my_text)