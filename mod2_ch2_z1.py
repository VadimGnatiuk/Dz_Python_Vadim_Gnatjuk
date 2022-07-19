'''
Задание 1
Пользователь вводит с клавиатуры номер дня недели
(1-7). Необходимо вывести на экран названия дня недели. Например, если 1,
то на экране надпись понедельник, 2 — вторник и т.д.
'''
'''
Введите номер дня недели:
Enter the number of the day of the week:
В неделе только 7 дней. Попробуйте запустить программу снова...
There are only 7 days in a week. Try running the program again...
'''
number_day_week = int(input("Enter the number of the day of the week : "))
if number_day_week == 1:
    print("It is Monday.")
elif number_day_week == 2:
    print("It's Tuesday.")
elif number_day_week == 3:
    print("It's Wednesday.")
elif number_day_week == 4:
    print("It's Thursday.")
elif number_day_week == 5:
    print("It's Friday.")
elif number_day_week == 6:
    print("It's Saturday.")
elif number_day_week == 7:
    print("This Sunday.")
else:
    print("There are only 7 days in a week. Try running the program again...")
