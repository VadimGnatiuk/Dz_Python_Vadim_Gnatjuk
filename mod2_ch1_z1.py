'''
Задание 1
Пользователь вводит с клавиатуры три числа.
В зависимости от выбора пользователя программа выводит
на экран сумму трёх чисел или произведение трёх чисел.
'''
# Вариант выбора                Choice option
# Сумма чисел составит          The sum of the numbers will be
# Запустите программу еще раз и повторите свой выбор...
# Run the program again and repeat your choice...
number_1 = float(input("Enter the first number : "))
number_2 = float(input("Enter the second number : "))
number_3 = float(input("Enter the third number : "))
sum_num = number_1 + number_2 + number_3
product_of_numbers = number_1 * number_2 * number_3
print("---"*33)
print("If you want to know the sum of numbers, then "
      "press \"1\", and if you want to know the product - \"2\".")
print("---"*33)
choice_option = int(input())
if choice_option == 1:
    print(f'The sum of the numbers will be {sum_num}.')
elif choice_option == 2:
    print(f'The product of the numbers will be {product_of_numbers}')
else:
    print("Run the program again and repeat your choice...")


