'''
Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число
в степень от нулевой до седьмой включительно.
'''
# Один нюанс - программу нужно писать только (???) через [if/elif/else] => (тогда смотри "mod2_ch3_z2.py")
number = float(input("Enter the number to be raised to the power (from 0 to 7): "))
degree_of = 0
while degree_of <= 7:
    print(f'The number you entered {number} to the power of {degree_of} is...', number ** degree_of)
    degree_of = degree_of + 1

