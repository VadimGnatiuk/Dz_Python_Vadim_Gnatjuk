'''
Задание 1
Дано два текстовых файла. Выяснить, совпадают ли их строки.
Если нет, то вывести несовпадающую строку из каждого файла.
'''

'''
Стихотворение           Poem
Иван Бунин "Тайна"      Ivan Bunin "The Secret"
Из ... строк ... строки обоих файлов не совпали, а ... строки - совпали.
From ... lines ... the lines of both files did not match, but ... the lines did.
Не совпали:             
'''

# Превратим тексты из файлов в два списка, каждый элемент которых - это отдельная строка.
# Let's turn texts from files into two lists, each element of which is a separate line.
f1 = open('poem1.txt', 'rt')
f2 = open('poem2.txt', 'rt')
a_list = f1.readlines()
b_list = f2.readlines()
f1.close()
f2.close()

count = 0
count_yes = 0
count_no = 0
if len(a_list) <= len(b_list):
    for i in range(len(a_list)):
        if a_list[i] != b_list[i]:
            print("Did not match:")
            print(a_list[i], b_list[i])
            count_no += 1
        else:
            count_yes += 1
        count += 1
    print(f'From {count} lines {count_no} the lines of both files did not match, but {count_yes} the lines did.')
else:
    for i in range(len(b_list)):
        if a_list[i] != b_list[i]:
            print("Did not match:")
            print(a_list[i], b_list[i])
            count_no += 1
        else:
            count_yes += 1
        count += 1
    print(f'From {count} lines {count_no} the lines of both files did not match, but {count_yes} the lines did.')
