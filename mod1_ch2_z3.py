# Задание 3
# Напишите программу, вычисляющую площадь ромба.
# Пользователь с клавиатуры вводит длину двух его диагоналей.
# Введите значение первой диагонали ромба
# Введите значение второй диагонали ромба
# Площадь ромба равна половине произведения его диагоналей: S = (AC · BD) / 2
# В таком случае, площадь ромба составит...
# Enter the value of the first diagonal of the rhombus
# Enter the value of the second diagonal of the rhombus
# In this case, the area of the rhombus will be...
diagonal1 = float(input("Enter the value of the first diagonal of the rhombus : "))
diagonal2 = float(input("Enter the value of the second diagonal of the rhombus : "))
area = (diagonal1 * diagonal2) / 2
print(f"In this case, the area of the rhombus will be... {area} .")

