'''
Задание 2
Пользователь вводит с клавиатуры три числа.
В зависимости от выбора пользователя программа выводит на экран максимум из трёх,
минимум из трёх или среднеарифметическое трёх чисел.
'''
'''
# Что Вас интересует (выберите соответствующую цифру)?)
# What are you interested in (select the appropriate number)?
#
# Наибольшее из трех чисел...               The largest of three numbers...
# Наименьшее из трех чисел...               The smallest of three numbers...
# Среднеарифметическое трех чисел...        The arithmetic mean of three numbers...
# если вы хотите определить наибольшее из трех чисел
# if you want to determine the largest of three numbers
# если вы хотите определить наименьшее из трех чисел
# if you want to determine the smallest of three numbers
# если вы хотите определить среднеарифметическое трех чисел
# if you want to find the average of three numbers
'''
number_1 = float(input("Enter the first number : "))
number_2 = float(input("Enter the second number : "))
number_3 = float(input("Enter the third number : "))
# --- Блок вычислений - Calculation block ---
if number_1 >= number_2:
    if number_2 >= number_3:
        largest = number_1
        smallest = number_3
if number_2 >= number_1:
    if number_1 >= number_3:
        largest = number_2
        smallest = number_3
if number_3 >= number_2:
    if number_2 >= number_1:
        largest = number_3
        smallest = number_1
arithmetic_mean = (number_1 + number_2 + number_3) / 3
# -------------------------------------------
print("==="*22)
print("What are you interested in (select the appropriate number)?")
print("press \"1\"- if you want to determine the largest of three numbers.")
print("press \"2\"- if you want to determine the smallest of three numbers.")
print("press \"3\"- if you want to find the average of three numbers.")
print("==="*22)
choice_option = int(input())
if choice_option == 1:
    print(f'The largest of three numbers... {largest}.')
elif choice_option == 2:
    print(f'The smallest of three numbers... {smallest}')
elif choice_option == 3:
    print(f'The arithmetic mean of three numbers... {arithmetic_mean}')
else:
    print("Run the program again and repeat your choice...")