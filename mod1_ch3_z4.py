'''
Задание 4
Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер
основания треугольника и размер высоты.
'''
# Для вычисления площади треугольника, введите значения основания треугольника
# и высоты, проведенной к этому основанию. S= 1/2 * ah.
# Введите величину основания треугольника:
# Введите значение высоты, проведенной к данному основанию:
# Тогда, площадь данного треугольника составит ...
# To calculate the area of a triangle, enter the base values of the triangle
# and the height drawn to this base.
# Enter the value of the base of the triangle:
# Enter the value of the height, drawn to the given base:
# Then, the area of this triangle will be ...
print("To calculate the area of a triangle, enter the base values of the triangle and \nthe height drawn to this base.")
osnov = float(input("Enter the value of the base of the triangle : "))
visot = float(input("Enter the value of the height, drawn to the given base : "))
area_tr = 1 / 2 * osnov * visot
print(f"Then, the area of this triangle will be ... {area_tr}.")
