#Распечатать все слова, в которых есть бука "о" и выбросить из текста, текст в конце рапечатать.

#решение ИИ:

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'

# Разделяем текст на слова (без удаления знаков препинания)
words = text.split()

# Слова с буквой "о"
words_with_o = [w for w in words if 'o' in w.lower()]

# Остальные слова (текст без слов с "о")
remaining_words = [w for w in words if 'o' not in w.lower()]

# Печать результатов
for word in words_with_o:
    print(word)

new_text = " ".join(remaining_words)
print("\nОставшийся текст:")
print(new_text)

#код Окулика
words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
        # words.remove(word)
    else:
        fin_words.append(word)

print(' '.join(words))

