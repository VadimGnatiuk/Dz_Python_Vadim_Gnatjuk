'''
Задание 6
Дан текстовый файл. Найти и заменить в нем заданное слово.
Что искать и на что заменять определяется пользователем.
'''

'''
Слово, которое ищем             The word we are looking for
Слово, на которое заменяем      The word to replace
Было совершено ... замен.       It was made ... substitutions.
для каждой строки текста        for each line of text
Результат работы сохранен в файле "poem_end.txt"        The result of the work is saved in the file "poem_end.txt"
'''
word = str(input('Enter the word we are looking for : '))
word_1 = str(input('Enter the word to replace : '))
count = 0

f = open('poem.txt', 'rt')
f_1 = open('poem_end.txt', 'wt')
for each_line_of_text in f:
    s = each_line_of_text.replace(f'{word}', f'{word_1}')
    if word in each_line_of_text:  # Let's count the number of replacements (Подсчитаем количество замен).
        count += 1
    f_1.write(s)
f_1.close()
f.close()

print()
print(f'It was made ... {count} substitutions.')
print(" *** " * 5)
print("The result of the work is saved in the file \"poem_end.txt\".")
print(" *** " * 5)
