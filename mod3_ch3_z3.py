'''
Задание 3
Подсчитать количество целых чисел в диапазоне от 100 до 9999
у которых все цифры разные.
'''
'''
Количество чисел        Amount of numbers
Количество целых чисел, у которых все цифры разные в диапазоне [100:9999] составляет...
The number of integers where all digits are different in the range [100:9999] is... 
'''
# Вариант 1, когда число рассматриваем как ЧИСЛО.
amount_of_numbers = 0
for i in range(100, 1000):
    x = i // 100
    y = i // 10 % 10
    z = i % 10
    #print("x = ", x)
    #print("y = ", y)
    #print("z = ", z)
    if x != y and x != z and y != z:
        amount_of_numbers += 1
    #print("amount_of_numbers =", amount_of_numbers)

for i in range(1000, 10000):
    x = i // 1000
    y = i // 100 % 10
    z = i // 10 % 10
    k = i % 10
    #print("x = ", x)
    #print("y = ", y)
    #print("z = ", z)
    #print("k = ", k)
    if x != y and x != z and x != k and y != z and y != k and z != k:
        amount_of_numbers += 1
    #print("amount_of_numbers =", amount_of_numbers)
print("---" * 30)
print(f' The number of integers where all digits are different in the range [100:9999] is... {amount_of_numbers}.')
