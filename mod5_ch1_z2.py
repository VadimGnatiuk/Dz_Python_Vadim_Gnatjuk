'''
Задание 2
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному файлу:
1 Количество символов;
2 Количество строк;
3 Количество гласных букв;
4 Количество согласных букв;
5 Количество цифр.
'''

'''
Гласные         Vowels
Согласные       Consonants
1 Количество символов;          1 Number of characters;
2 Количество строк;             2 Number of lines;
3 Количество гласных букв;      3 Number of vowels;
4 Количество согласных букв;    4 Number of consonants;
5 Количество цифр.              5 Number of digits.

'''
count_of_chars = 0
count_of_lines = 0
vowels_of_letters = 'ауоыэяюёие'
count_vowels_of_letters = 0
consonants_of_letters = 'бвгджзйклмнпрстфхцчшщ'
count_consonants_of_letters = 0
numbers = '0123456789'
count_of_digits = 0

# Crate("write") a new file is name "poem.txt"
f = open('poem.txt', 'wt')
f.write('''Тайна
Он на клинок дохнул — и жало
Его сирийского кинжала
Померкло в дымке голубой:
Под дымкой ярче заблистали
Узоры золота на стали
Своей червонною резьбой.

«Во имя Бога и пророка.
Прочти, слуга небес и рока,
Свой бранный клич: скажи, каким
Девизом твой клинок украшен?»
И он сказал: «Девиз мой страшен.
Он — тайна тайн: Элиф. Лам. Мим».

«Элиф. Лам. Мим? Но эти знаки
Темны, как путь в загробном мраке:
Сокрыл их тайну Мохаммед...»
«Молчи, молчи! — сказал он строго, —
Нет в мире Бога, кроме Бога,
Сильнее тайны — силы нет».

Сказал, коснулся ятаганом
Чела под шелковым тюрбаном,
Окинул жаркий Атмейдан[3]
Ленивым взглядом хищной птицы —
И тихо синие ресницы
Опять склонил на ятаган.

Иван Алексеевич Бунин
1905''')
f.close()

# Determine the number of characters in the source file "poem.txt":
# Определим количество символов в исходном файле "poem.txt":
f = open('poem.txt', 'rt')
count_of_chars = len(f.read())
f.close()
print(f'Number of characters ... {count_of_chars}.')

# Determine the number of lines in the source file "poem.txt":
# Определим количество строк в исходном файле "poem.txt":
f = open('poem.txt', 'rt')
count_of_lines = len(f.readlines())
f.close()
print(f'Number of lines ... {count_of_lines}.')

# Determine the number of vowels in the source file "poem.txt":
# Определим количество гласных букв в исходном файле "poem.txt":
#line_i = ''
f = open('poem.txt', 'rt')
char = f.read(1)
while char:
    #print(char)
    if char.lower() in vowels_of_letters.lower():
        count_vowels_of_letters += 1
    char = f.read(1)
f.close()
print(f'Number of vowels ... {count_vowels_of_letters}.')

# Determine the number of consonants in the source file "poem.txt":
# Определим количество согласных букв в исходном файле "poem.txt":
#line_i = ''
f = open('poem.txt', 'rt')
char = f.read(1)
while char:
    #print(char)
    if char.lower() in consonants_of_letters.lower():
        count_consonants_of_letters += 1
    char = f.read(1)
f.close()
print(f'Number of consonants ... {count_consonants_of_letters}.')

# Determine the number of digits in the source file "poem.txt":
# Определим количество цифр в исходном файле "poem.txt":
#line_i = ''
f = open('poem.txt', 'rt')
char = f.read(1)
while char:
    #print(char)
    if char.lower() in numbers:
        count_of_digits += 1
    char = f.read(1)
f.close()
print(f'Number of digits ... {count_of_digits}.')

f_stat = open('file_statistics.txt','wt')
f_stat.write("Source file statistics : \n")
f_stat.write("______________________________\n")
f_stat.write(f'Number of characters ... {count_of_chars}.\n')
f_stat.write(f'Number of lines ... {count_of_lines}.\n')
f_stat.write(f'Number of vowels ... {count_vowels_of_letters}.\n')
f_stat.write(f'Number of consonants ... {count_consonants_of_letters}.\n')
f_stat.write(f'Number of digits ... {count_of_digits}.')
f_stat.close()