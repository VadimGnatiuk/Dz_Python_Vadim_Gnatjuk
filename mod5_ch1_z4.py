'''
Задание 4
Дан текстовый файл. Найти длину самой длинной строки.
'''

'''
Длина самой длинной строки в файле      The length of the longest line in the file
'''

f = open('poem.txt', 'rt')
list_of_lines = f.readlines()# Turned a text file into a list of strings(Превратили текстовый файл в список из строк).
f.close()
#print(list_of_lines)

max_line_i = len(list_of_lines[0])
#print(max_line_i)

for i in range(len(list_of_lines)):
    if len(list_of_lines[i]) > max_line_i:
        max_line_i = len(list_of_lines[i])

print(f'The length of the longest line in the file ... {max_line_i} characters.')
