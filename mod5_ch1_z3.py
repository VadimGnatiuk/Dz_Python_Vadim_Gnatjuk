'''
Задание 3
Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.
'''

# # Variant_1
# f = open('poem.txt', 'rt')
# list_of_lines = f.readlines()# Turned a text file into a list of strings(Превратили текстовый файл в список из строк).
# f.close()
# print(list_of_lines)
#
# f_end = open('file_without_last_line.txt','wt')
# f_end.write(str(list_of_lines[:-1]))
# f_end.close()

# Variant_2
f = open('poem.txt', 'rt')
l = len(f.readlines())  # Total number of lines in the file (Общее количество строк в файле)
f.close()

f = open('poem.txt', 'rt')
f_end = open('file_without_last_line.txt', 'wt')
for i in range(l):
    if i < (l - 1):
        f_end.write(f.readline())
f_end.close()
f.close()
