'''
Задание 3
Пользователь вводит с клавиатуры число. Если число
больше нуля нужно вывести надпись «Number is positive»,
если меньше нуля «Number is negative», если равно нулю
«Number is equal to zero».
'''
number = float(input("Enter the number : "))
if number > 0:
    print("«Number is positive».")
elif number < 0:
    print("«Number is negative».")
else:
    print("«Number is equal to zero».")