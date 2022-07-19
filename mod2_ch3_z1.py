'''
Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz.
Если число кратно 3 и 5 нужно вывести Fizz Buzz.
Если число не кратно не 3 и 5 нужно вывести само число.
Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.
'''
'''
enter a number between 1 and 100.
'''
# first way - первый способ

number = int(input("Enter a number between 1 and 100 : "))
if (number < 1) or (number > 100): # option when it works in case of False - вариант, когда работает в случае False
    print("************************************************************************************")
    print("Error. You entered a number out of range (or not an integer). Run the program again.")
    print("************************************************************************************")
elif (number % 3 == 0) and (number % 5 == 0):
    print("Fizz Buzz")
elif (number % 3 != 0) and (number % 5 != 0):
    print(number)
elif (number % 3 == 0):
    print("Fizz")
elif (number % 5 == 0):
    print("Buzz")

