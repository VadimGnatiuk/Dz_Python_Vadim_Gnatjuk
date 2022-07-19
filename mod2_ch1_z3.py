'''
Задание 3
Пользователь вводит с клавиатуры количество метров.
В зависимости от выбора пользователя программа
переводит метры в мили, дюймы или ярды.
'''
'''
Укажите длинну, выраженную в метрах:
Specify the length expressed in meters:

Если Вы хотите выразить длинну в милях
If you want to express the length in miles
Если Вы хотите выразить длину в дюймах
If you want to express length in inches
Если Вы хотите выразить длину в ярдах
If you want to express the length in yards

# Что Вас интересует (выберите соответствующую цифру)?)
# What are you interested in (select the appropriate number)?

Длинна, указанная Вами в метрах, соответствует ... милям.
The length indicated by you in meters corresponds to ... miles.
Длинна, указанная Вами в метрах, соответствует ... дюймам.
The length indicated by you in meters corresponds to ... inches.
Длинна, указанная Вами в метрах, соответствует ... ярдам.
The length indicated by you in meters corresponds to ... yards.
'''
length = float(input("Specify the length expressed in meters : "))
# ----------------------------------------------------------------
print("=== "*15)
print("What are you interested in (select the appropriate number)?")
print("press \"1\"- If you want to express the length in miles.")
print("press \"2\"- If you want to express length in inches.")
print("press \"3\"- If you want to express the length in yards.")
print("=== "*15)
choice_option = int(input())
if choice_option == 1:
    print(f'The length indicated by you in meters corresponds to {length/1609} miles.')
elif choice_option == 2:
    print(f'The length indicated by you in meters corresponds to {length*39.37} inches.')
elif choice_option == 3:
    print(f'The length indicated by you in meters corresponds to {length*1.094} yards.')
else:
    print("Run the program again and repeat your choice...")\

