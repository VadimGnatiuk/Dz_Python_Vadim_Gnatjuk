'''
Задание 2
Подсчитать количество целых чисел в диапазоне
от 100 до 999 у которых есть две одинаковые цифры.
'''
'''
Количество чисел        Amount of numbers
Количество целых чисел, у которых есть две одинаковые цифры в диапазоне [100:999] составляет...
The number of integers that have two identical digits in the range [100:999] is... 
'''
# Вариант 1, когда число рассматриваем как ЧИСЛО.
amount_of_numbers = 0
for i in range(100, 1000):
    x = i // 100
    y = i // 10 % 10
    z = i % 10
    # print("x = ", x)
    # print("y = ", y)
    # print("z = ", z)
    if x == y or x == z or y == z:
        amount_of_numbers += 1
print("---" * 30)
print(f'  The number of integers that have two identical digits in the range [100:999] is... {amount_of_numbers}.')
