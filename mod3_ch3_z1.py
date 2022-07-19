'''
Задание 1
Напишите программу, которая запрашивает два целых числа x и y,
после чего вычисляет и выводит значение x в степени y.
'''
'''
Введите основание степени числа :               Enter the base of the degree of the number:
Введите степень числа :                         Enter the degree of the number :
Число Х в степени У равняется...                The number X to the power of Y equals...
[Проверка работоспособности цикла: x**y = ]     [Loop health check: x**y = ]
'''

x = int(input("Enter the base of the degree of the number : "))
y = int(input("Enter the degree of the number : "))
degree = 1
if y < 0:
    for i in range(-y):
        degree = degree * (1 / x)
        #print(degree)
else:
    for i in range(y):
        degree = degree * x
        #print(degree)
print(". . ." * 9)
print(f'The number {x} to the power of {y} equals... {degree}.')
print(". . ." * 9)
print("___" * 25)
print(f'[Loop health check: {x} ** {y} = {x ** y}].')
