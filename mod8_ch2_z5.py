'''
Задание 5
Существует два множества, содержащие названия городов.
Необходимо создать третье множество, содержащее уникальные названия для каждого множества.
'''
'''
Элементы, которые уникальны для каждого множества:
Elements that are unique for each set:
'''
set_one = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw', 'WWWWW'}
set_two = {'Paris', 'Berlin', 'AAAA', 'Rome', 'Madrid', 'Kiev', 'London', 'Warsaw', 'Riga', 'Vilnyus', 'Tallinn'}
print("set_one = ", set_one)
print("set_two = ", set_two)
print("____" * 28)
print("Elements that are unique for each set:")
# var-1 -------------------------------------------------
# set_three = set_two ^ set_one
# print(set_three)
# -------------------------------------------------------
# var-2 -------------------------------------------------
# set_two ^= set_one
# print(set_two)
# -------------------------------------------------------
# var-3 -------------------------------------------------
set_three = set_one.symmetric_difference(set_two)
print(set_three)
# -------------------------------------------------------
