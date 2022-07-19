'''
Задание 2
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5.
'''
'''
Указанный диапазон содержит следующие числа :   The specified range contains the following numbers:
Все числа диапазона в убывающем порядке :       All numbers in the range in descending order:
Все числа, кратные 7:                           All numbers that are multiples of 7:
Количество чисел, кратных 5:                    Number of multiples of 5       
Счетчик                                         Counter
'''

x = float(input('Enter the start of a range of numbers : '))
y = float(input('Enter the end of the range of numbers : '))

if x != int(x) or y != int(y):  # --- Проверка числа на "целое": (Checking a number for "integer":)
    print("---" * 21)
    print("It is better to use only INTEGER numbers! Run the program again.")
else:
    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("..." * 23)
    print("The specified range contains the following numbers:")
    while i <= y:
        print(i, end=' ')
        i += 1
    print()

    i = y  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("..." * 23)
    print("All numbers in the range in descending order:")
    while i >= x:
        print(i, end=' ')
        i -= 1
    print()

    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("---" * 23)
    print("All numbers that are multiples of 7: ")
    while i <= y:
        if i == 0:
            i += 1
            # continue # с учетом предыдущей строки - можно не использовать
        if i % 7 == 0:
            print(i, end=' ')
        i = i + 1
    print()

    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    count_5 = 0 # Обнуляем счетчик чисел (Resetting the number counter)
    print("---" * 23)
    print("Number of multiples of 5: ")
    while i <= y:
        if i == 0:
            i += 1
            # continue # с учетом предыдущей строки - можно не использовать
        if i % 5 == 0:
            #print(i, end=' ')
            count_5 = count_5 + 1
        i = i + 1
    print(f'count_5 = {count_5}.')

