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
# Вариант 2, когда число рассматриваем как ЧИСЛИТЕЛЬНОЕ, т.е. текст.
amount_of_numbers = 0
for i in range(100, 1000):
    a, b, c = str(i)
    #print("a = ", a)
    #print("b = ", b)
    #print("c = ", c)
    if a != b and a != c and b != c:
        amount_of_numbers += 1
    #print("amount_of_numbers =", amount_of_numbers)

for i in range(1000, 10000):
    a, b, c, d = str(i)
    #print("a = ", a)
    #print("b = ", b)
    #print("c = ", c)
    #print("d = ", d)
    if a != b and a != c and a != d and b != c and b != d and c != d:
        amount_of_numbers += 1
    #print("amount_of_numbers =", amount_of_numbers)
print("---" * 30)
print(f' The number of integers where all digits are different in the range [100:9999] is... {amount_of_numbers}.')
