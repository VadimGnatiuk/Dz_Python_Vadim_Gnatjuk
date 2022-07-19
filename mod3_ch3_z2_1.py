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
# Вариант 2, когда число рассматриваем как ЧИСЛИТЕЛЬНОЕ, т.е. текст.
amount_of_numbers = 0
# a = b = c = ''
for i in range(100, 1000):
    a, b, c = str(i)
    # print("a = ", a)
    # print("b = ", b)
    # print("c = ", c)
    if a == b or a == c or b == c:
        amount_of_numbers += 1
print("---" * 30)
print(f'  The number of integers that have two identical digits in the range [100:999] is... {amount_of_numbers}.')
