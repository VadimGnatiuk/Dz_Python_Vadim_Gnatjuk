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

list_one = list(range(-9, 9, 2))
list_two = list(range(15))
# 1 Сформировать третий список, содержащий элементы обоих списков;
print("1.", "+ +" * 26)
list_temp = list_two[:]  # make a copy of the second list, which will be gradually "cut off" (via "pop()").
list_three = list_one[:]
while list_temp:
    elem = list_temp.pop(0)
    list_three.append(elem)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'Сформировать третий список, содержащий элементы обоих списков;')
print(list_three)
print("1.", "+ +" * 26)

# 2 Сформировать третий список, содержащий элементы обоих списков без повторений;
print()
print("2.", " *** " * 16)
list_three_1 = list_one[:]
b = list_two[:]
while b:
    e_two = b.pop(0)
    if e_two not in list_one:
        list_three_1.append(e_two)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий элементы обоих списков без повторений;')
print(list_three_1)
print("2.", " *** " * 16)

# 3. Сформировать третий список, содержащий элементы общие для двух списков;
list_one = [1, -5, 1, 'yoy', 90, 1, 30, 1, 1]
list_two = [-1, 1, -2, 0, 90, 7, 1, 5, 30, 4, 1]
print()
print("3.", "___" * 26)

list_three_2 = []
a = list_one[:]
b = list_two[:]

while a:  # перебираем все элементы в первом списке
    e_one = a.pop(0)
    if e_one in list_two and e_one not in list_three_2:  # если такой элемент(из первого списка) встречается во
        # втором списке (и его еще небыло в результирующем...)
        list_three_2.append(e_one)  # то нужно его добавить в результирующий.

while b:  # перебираем все элементы из второго списка
    e_two = b.pop(0)
    if e_two in list_two and e_two not in list_three_2:  # если такой элемент(из первого списка) встречается во
        # втором списке (и его еще небыло в результирующем...)
        list_three_2.append(e_two)  # то нужно его добавить в результирующий.

# Ещё нужно проверить повторяющиеся элементы (в первом - пять едениц, а во втором - три => в результирующем
# списке должно быть тоже три):
for e_three in list_three_2:  # для каждого элемента результирующего списка - если ОН ("e_three")
    if list_one.count(e_three) > list_three_2.count(e_three) and list_two.count(e_three) > list_three_2.count(e_three):
        if list_one.count(e_three) <= list_two.count(e_three):
            for i in range(list_one.count(e_three) - 1):
                list_three_2.append(e_three)
        else:
            for i in range(list_two.count(e_three) - 1):
                list_three_2.append(e_three)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'Сформировать третий список, содержащий элементы общие для двух списков;')
print(list_three_2)
print("3.", "___" * 26)

# 4. Сформировать третий список, содержащий только уникальные элементы каждого из списков;
print()
print("4.", "+++" * 29)
list_three_3 = []
a = list_one[:]
b = list_two[:]
while a:# перебираем все элементы в первом списке
    e_one = a.pop(0)
    if e_one not in list_two and e_one not in list_three_3:
        list_three_3.append(e_one)
while b:# перебираем все элементы во втором списке
    e_two = b.pop(0)
    if e_two not in list_one and e_two not in list_three_3:
        list_three_3.append(e_two)
print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий только уникальные элементы каждого из списков;')
print(list_three_3)
print("4.", "+++" * 29)

# 5. Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
print()
print("5.", "..." * 34)
list_three_4 = []
min_one = list_one[0]
max_one = list_one[0]
min_two = list_two[0]
max_two = list_two[0]
i = 0
while i < len(list_one):
    if str(list_one[i]) < str(min_one):
        min_one = list_one[i]
    if str(list_one[i]) > str(max_one):
        max_one = list_one[i]
    i += 1
# print(min_one)
# print(max_one)
i = 0
while i < len(list_two):
    if str(list_two[i]) < str(min_two):
        min_two = list_two[i]
    if str(list_two[i]) > str(max_two):
        max_two = list_two[i]
    i += 1
# print(min_two)
# print(max_two)

list_three_4.append(min_one)
list_three_4.append(max_one)
list_three_4.append(min_two)
list_three_4.append(max_two)

print(f'List 1 = {list_one}.')
print(f'List 2 = {list_two}.')
print(f'\tСформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.')
print(list_three_4)
print("5.", "..." * 34)
