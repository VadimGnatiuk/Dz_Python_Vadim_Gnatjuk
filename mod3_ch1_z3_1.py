'''
Задание 3
(Второй вариант - когда условия проверяются-выполняются потоком (в одном и том же списке чисел).)
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне.
Вывод на экран должен проходить по правилам, указанным ниже.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz.
Если число кратно 3 и 5 нужно вывести Fizz Buzz.
Если число не кратно не 3 и 5 нужно вывести само число.
'''
'''
Анализ всех чисел в этом диапазоне, показывает следующее:
Analysis of all numbers in this range reveals the following:
'''
x = float(input('Enter the start of a range of numbers : '))
y = float(input('Enter the end of the range of numbers : '))

if x != int(x) or y != int(y):  # --- Проверка числа на "целое": (Checking a number for "integer":)
    print("---" * 21)
    print("It is better to use only INTEGER numbers! Run the program again.")
else:
    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("..." * 23)
    print("Analysis of all numbers in this range reveals the following:")
    while i <= y:
        if i == 0:
            print(i, end=' ')
        elif (i % 3 == 0) and (i % 5 == 0):
            #print(i, end=' ')
            print("\"Fizz Buzz\"", end=' ')
        elif i % 3 == 0:
            #print(i, end=' ')
            print("Fizz", end=' ')
        elif i % 5 == 0:
            #print(i, end=' ')
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
        i += 1
    print()
    print("..." * 23)

