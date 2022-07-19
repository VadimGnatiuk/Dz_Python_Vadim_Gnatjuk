'''
Задание 1
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне по следующему правилу:
если число кратно 7, его надо выводить на экран
'''
'''
Введите начало диапазона чисел :                    Enter the start of a range of numbers : 
Введите конец диапазона часел :                     Enter the end of the range of numbers : 
В указанном диапазоне следующие числа кратны 7 : Within the specified range, the following numbers are multiples of 7:
Лучше использовать только ЦЕЛЫЕ числа! Запустите программу ещё раз.
It is better to use only INTEGER numbers! Run the program again.
'''
x = float(input('Enter the start of a range of numbers : '))
y = float(input('Enter the end of the range of numbers : '))

if x != int(x) or y != int(y):  #--- Проверка числа на "целое": (Checking a number for "integer":)
    print("---" * 21)
    print("It is better to use only INTEGER numbers! Run the program again.")
else:
    i = x  # Fixing the beginning of a range of numbers (Фиксируем начало диапазона чисел)
    print("---" * 23)
    print("Within the specified range, the following numbers are multiples of 7: ")
    print("---" * 23)
    while i <= y:
        if i == 0:
            i += 1
            #continue # с учетом предыдущей строки - можно не использовать
        if i % 7 == 0:
            print(i, end=' ')
        i = i + 1
