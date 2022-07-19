'''
Задание 2
Существует два множества, содержащие названия городов.
Необходимо создать третье множество, содержащее названия,
которые есть в обоих множествах.
'''
'''
В обоих множествах содержатся следующие ОБЩИЕ елементы:     Both sets contain the following COMMON elements:
'''
set_one = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw'}
set_two = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw', 'Riga', 'Vilnyus', 'Tallinn'}
print("set_one = ", set_one)
print("set_two = ", set_two)
print("____" * 28)
print("Both sets contain the following COMMON elements:")
# var-1 -------------------------------------------------
# set_three = set_one & set_two
# print(set_three)
# -------------------------------------------------------
# var-2 -------------------------------------------------
# set_one &= set_two
# print(set_one)
# -------------------------------------------------------
# var-3 -------------------------------------------------
set_three = set_one.intersection(set_two)
print(set_three)
# -------------------------------------------------------
