'''
Задание 3
Существует два множества, содержащие названия городов.
Необходимо создать третье множество, содержащее названия, которые есть в первом множестве,
но нет во втором.
'''
'''
Элементы, которые есть в первом множестве, но отсутствуют во втором:
Elements that are in the first set but not in the second:
'''
set_one = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw', 'Riga', 'Vilnyus', 'Tallinn'}
set_two = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw'}
print("set_one = ", set_one)
print("set_two = ", set_two)
print("____" * 28)
print("Elements that are in the first set but not in the second:")
# var-1 -------------------------------------------------
# set_three = set_one - set_two
# print(set_three)
# -------------------------------------------------------
# var-2 -------------------------------------------------
# set_one -= set_two
# print(set_one)
# -------------------------------------------------------
# var-3 -------------------------------------------------
set_three = set_one.difference(set_two)
print(set_three)
# -------------------------------------------------------
