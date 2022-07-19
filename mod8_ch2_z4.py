'''
Задание 4
Существует два множества, содержащие названия городов.
Необходимо создать третье множество, содержащее названия,
которые есть во втором множестве, но нет в первом.
'''
'''
Элементы, которые есть во втором множестве, но отсутствуют в первом:
Elements that are in the first set but not in the second:
'''
set_one = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw'}
set_two = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw', 'Riga', 'Vilnyus', 'Tallinn'}
print("set_one = ", set_one)
print("set_two = ", set_two)
print("____" * 28)
print("Elements that are in the second set but not in the first:")
# var-1 -------------------------------------------------
# set_three = set_two - set_one
# print(set_three)
# -------------------------------------------------------
# var-2 -------------------------------------------------
# set_two -= set_one
# print(set_two)
# -------------------------------------------------------
# var-3 -------------------------------------------------
set_three = set_two.difference(set_one)
print(set_three)
# -------------------------------------------------------
