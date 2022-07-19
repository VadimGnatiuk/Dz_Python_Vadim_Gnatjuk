'''
Задание 5
Пользователь с клавиатуры вводит четырёхзначное
число. Необходимо перевернуть число и отобразить результат.
Например, если введено 4512, результат 2154.
'''
# Введите целое четырехзначное число:
# Введенное число состоит из ___ цифр.
# Тогда, число-перевертыш получится...
# Enter a four-digit integer number:
# The entered number consists of ___ digits.
# Then, the flip-number will be...
four_dig_num = int(input("Enter a four-digit integer number : "))
number_1 = four_dig_num // 1000
number_2 = four_dig_num // 100 % 10
number_3 = four_dig_num // 10 % 10
number_4 = four_dig_num % 10
print('The entered number {} consists of {} {} {} {} '
      'digits.'.format(four_dig_num, number_1, number_2, number_3, number_4))
flip_num = number_4 * 1000 + number_3 * 100 + number_2 * 10 + number_1
print(f'Then, the flip-number will be... {flip_num}.')
