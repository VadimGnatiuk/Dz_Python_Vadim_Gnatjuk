'''
Задание 3
(Первый вариант - когда условия проверяются-выполняются по ОТДЕЛЬНОСТИ.)
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне.
Вывод на экран должен проходить по правилам, указанным ниже.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz.
Если число кратно 3 и 5 нужно вывести Fizz Buzz.
Если число не кратно не 3 и 5 нужно вывести само число.
'''
'''
Числа кратные 3:        Multiples of 3:
'''
x = float(input('Enter the start of a range of numbers : '))
y = float(input('Enter the end of the range of numbers : '))

if x != int(x) or y != int(y):  # --- Проверка числа на "целое": (Checking a number for "integer":)
    print("---" * 21)
    print("It is better to use only INTEGER numbers! Run the program again.")
else:
    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("..." * 23)
    print("Multiples of 3:")
    while i <= y:
        if i == 0:
            i += 1
            # continue # с учетом предыдущей строки - можно не использовать
        if i % 3 == 0:
            #print(i, end=' ')
            print("Fizz", end=' ')
        i += 1
    print()

    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("..." * 23)
    print("Multiples of 5:")
    while i <= y:
        if i == 0:
            i += 1
            # continue # с учетом предыдущей строки - можно не использовать
        if i % 5 == 0:
            #print(i, end=' ')
            print("Buzz", end=' ')
        i += 1
    print()

    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("..." * 23)
    print("Multiples of 3 and 5 (and NOT):")
    while i <= y:
        if i == 0:
            i += 1
            # continue # с учетом предыдущей строки - можно не использовать
        if (i % 3 == 0) and (i % 5 == 0):
            #print(i, end=' ')
            print("\"Fizz Buzz\"", end=' ')
        else:
            print(i, end=' ')
        i += 1
    print()

