'''
Задание 2
Пользователь вводит с клавиатуры число, состоящее из четырех цифр.
Требуется найти произведение цифр. Например, если с клавиатуры
введено 1324, тогда результат произведения 1*3*2*4 = 24.
'''
# Введите целое четырехзначное число
# Данное число состоит из следующих цифр
# тогда, произведение цифр данного числа равно
# Enter an integer four-digit number
# This number consists of the following digits
# then, the product of the digits of the given number is
number = int(input("Enter an integer four-digit number : "))
number_1 = number // 1000
number_2 = number // 100 % 10
number_3 = number // 10 % 10
number_4 = number % 10
print(f'This number, {number}, consists of the following digits:\n{number_1}, {number_2}, {number_3}, {number_4},')
product_of_the_digits = number_1 * number_2 * number_3 * number_4
print(f'then, the product of the digits of the given number is... {product_of_the_digits}.')
