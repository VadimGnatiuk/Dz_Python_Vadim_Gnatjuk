'''
Задание 1
Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры.
Например, если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.
'''
# Введите количество сотен будующего числа
# Введите количество десятков будующего числа
# Введите количество едениц будующего числа
# Enter the number of hundreds of the future number
# Enter the number of tens of the future number
# Enter the number of units of the future number
number1 = int(input('Enter the number of hundreds of the future number : '))
number2 = int(input('Enter the number of tens of the future number : '))
number3 = int(input('Enter the number of units of the future number : '))
print(number1 * 100 + number2 * 10 + number3)
