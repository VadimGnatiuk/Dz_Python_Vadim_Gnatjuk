'''
Задание 4
Пользователь вводит два числа. Определить, равны ли эти числа,
и, если нет, вывести их на экран в порядке возрастания.
'''
number_1 = float(input("Enter the first number : "))
number_2 = float(input("Enter the second number : "))
if number_1 > number_2:
    print(number_2, number_1)
elif number_2 > number_1:
    print(number_1, number_2)
else:
    print("These numbers are equal.")
