# Домашнее задание 1; Гнатюк Вадим; Gnatjuk Vadim
# Создать 4 переменных разных типов и указать в них данные.
# Например: color, age, animal, alcohol и так далее.
# С использованием данных переменных написать программу,
# которая выводит текст, по аналогии с тем, как делали на паре.
#
#
# косинус угла -        cosine of angle     float       cos_angl
# прилежащий катет -    adjacent leg        int         leg_adj
# гипотенуза -          hypotenuse          int         hyp
# согласны д/н          agree y/n           bolean      agree
# Тригонометрия -       Trigonometry        str         name
# Одно из тригонометрических выражений, а именно косинус угла, находится как отношение
# прилежащего катета к гипотенузе.
# ******************** В нашем случае: косинус_угла = прил_кат / гипотен.
# Вы согласны с данным утверждением?

# One of the trigonometric expressions
# namely, the cosine of the angle is found as the ratio
# adjacent leg to the hypotenuse.
# ******************** In our case: cosine_of_angle = app_cat / hypoten.
# Do you agree with this statement?


name = 'trigonometric'
leg_adj = int(input("Прилежащий катет : "))
hyp = int(input("Гипотенуза : "))
cos_angl = leg_adj / hyp
agree = bool(input("Вы согласны (1/0): ")) #Почему результат всегда - true???
print(f'One of the {name} expressions namely, the cosine of the angle, is found as the ratio adjacent leg to the hypotenuse.')
print(f'In our case: {cos_angl} = {leg_adj} / {hyp}.')
print(f'Do you agree with this statement? - {agree}')
print('name - ', type(name))
print('leg_adj - ', type(leg_adj))
print('hyp - ', type(hyp))
print('cos_angl - ', type(cos_angl))
print('agree - ', type(agree))
