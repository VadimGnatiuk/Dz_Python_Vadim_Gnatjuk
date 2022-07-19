'''
Задание 2
Пользователь вводит с клавиатуры номер месяца (1-12).
Необходимо вывести на экран название месяца.
Например, если 1, то на экране надпись январь, 2 — февраль и т.д.
'''
'''
Введите номер месяца:
Enter month number:
В году только 12 месяцев. Попробуйте запустить программу снова...
There are only 12 months in a year. Try running the program again...
'''
number_month = int(input("Enter month number : "))
if number_month == 1:
    print("This is the number of January.")
elif number_month == 2:
    print("This is the serial number of February.")
elif number_month == 3:
    print("This is the serial number of March.")
elif number_month == 4:
    print("This is the serial number of April.")
elif number_month == 5:
    print("This is the serial number of May.")
elif number_month == 6:
    print("This is the number of June.")
elif number_month == 7:
    print("This is the serial number of July.")
elif number_month == 8:
    print("This is the number of August.")
elif number_month == 9:
    print("This is the serial number of September.")
elif number_month == 10:
    print("This is the number of October.")
elif number_month == 11:
    print("This is the serial number of November.")
elif number_month == 12:
    print("This is the serial number of December.")
else:
    print("There are only 12 months in a year. Try running the program again...")
