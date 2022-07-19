'''
Модуль 4. Строки. Списки.
Часть 3 Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
■ 1. Сформировать третий список, содержащий элементы обоих списков;
■ 2. Сформировать третий список, содержащий элементы обоих списков
 без повторений;
■ 3. Сформировать третий список, содержащий элементы общие для двух списков;
■ 4. Сформировать третий список, содержащий только уникальные
 элементы каждого из списков;
■ 5. Сформировать третий список, содержащий только минимальное
 и максимальное значение каждого из списков.
'''
# 1. Сформировать третий список, содержащий элементы обоих списков;
list_one = list(range(-9, 9, 2))
list_two = list(range(15))
print(f'list_one = {list_one}.')
print(f'list_two = {list_two}.')
print("1.", "- -" * 26)
print(f'\tСформировать третий список, содержащий элементы обоих списков;')
list_three = list_one + list_two
print(list_three)
print("1.", "- -" * 26)

# 2 Сформировать третий список, содержащий элементы обоих списков без повторений;
print()
print("2.", " *** " * 16)
list_three_1 = list_one[:]
for e_two in list_two:
    if e_two not in list_one:
        list_three_1.append(e_two)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий элементы обоих списков без повторений;')
print(list_three_1)
print("2.", " *** " * 16)

# 3. Сформировать третий список, содержащий элементы общие для двух списков;
#list_one = [1, -5, 1, 'yoy', 90, 1, 30, 1, 1]
#list_two = [-1, 1, -2, 0, 90, 7, 1, 5, 30, 4, 1]
list_three_2 = list(set(list_one) & set(list_two))
print()
print("3.", "___" * 26)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий элементы общие для двух списков;')
print(list_three_2)
print("3.", "___" * 26)

# 4. Сформировать третий список, содержащий только уникальные элементы каждого из списков;
print()
print("4.", "+++" * 29)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий только уникальные элементы каждого из списков;')
list_three_3 = []
for e_one in list_one:  # перебираем все элементы в первом списке
    if e_one not in list_two and e_one not in list_three_3:
        list_three_3.append(e_one)
for e_two in list_two:  # перебираем все элементы в первом списке
    if e_two not in list_one and e_two not in list_three_3:
        list_three_3.append(e_two)
print(list_three_3)
print("4.", "+++" * 29)

# 5. Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
print()
print("5.", "..." * 34)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.')
# print(list_one)
# print(list_two)
list_three_4 = []

list_three_4.append(min(list_one))
list_three_4.append(max(list_one))
list_three_4.append(min(list_two))
list_three_4.append(max(list_two))
print(list_three_4)
print("5.", "..." * 34)
