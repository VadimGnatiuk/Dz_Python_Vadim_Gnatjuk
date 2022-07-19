'''
Задание 4
Пользователь вводит любое целое число.
Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести
обратно на экран.
'''
'''
Введите любое целое число :         Enter any integer :
Исходное число..., а результирующее (без \"3\" и \"6\")...
The original number is..., and the resulting number (without \"3\" and \"6\")...
'''
number = int(input("Enter any integer : "))
number_str = str(number)    # Превратим число в строку (хотя этого можно и не делать(Правда, Андрей?),
                            # а сразу вводить число как строковую переменную (в предыдущей команде).
s = ''
for letter in number_str:
    if letter == '3' or letter == '6':
        s = s + ''
    else:
        s = s + letter
print(f'The original number is {number_str}, and the resulting number (without \"3\" and \"6\") {s}.')
#print(number_str)
#print(s)
