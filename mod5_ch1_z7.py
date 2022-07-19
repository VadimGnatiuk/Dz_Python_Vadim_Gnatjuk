'''
Задание 7
Напишите функцию, которая проверяет является ли число палиндромом.
Число передаётся в качестве параметра.
Если число палиндром нужно вернуть из функции true, иначе false.
«Палиндром» — это число, у которого первая часть цифр равна второй
перевернутой части цифр.
Например, 123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром, а 421987 — не палиндром.
'''

'''
первая половина числа       first half of the number
Количество цифр в числе непарное. Число не может быть палиндромом!
The number of digits in a number is unpaired. A number cannot be a palindrome!
Данное число - палиндром!   This number is palindrome!
Данное число НЕ палиндром.  This number is NOT a palindrome.
'''


# x = int(input("Enter number : "))

def whether_the_number_is_a_palindrome(x):
    if x < 0:
        x = str(x)
        x = x[1:]
        x = int(x)
        # print(x)

    x_str = str(x)
    if len(x_str) % 2 == 0:
        f_h = int(len(x_str) / 2)
        s_h = int(len(x_str) / 2)
        first_half_number = x_str[:f_h]
        second_half_number = x_str[s_h:]
        print(f_h, s_h, sep=' ___ ', )
        print(first_half_number, second_half_number, sep=' ___ ')
        second_half_number_1 = second_half_number[::-1]  # turn over the number
        print(first_half_number, second_half_number_1, sep=' ___ ')
        if first_half_number == second_half_number_1:
            print("This number is palindrome!")
            print()
        else:
            print("This number is NOT a palindrome.")
            print()
    else:
        # print(len(x_str) % 2)
        print("The number of digits in a number is unpaired. A number cannot be a palindrome!")
        print()


whether_the_number_is_a_palindrome(123456)
whether_the_number_is_a_palindrome(-123456)
whether_the_number_is_a_palindrome(9876543)
whether_the_number_is_a_palindrome(1221)
whether_the_number_is_a_palindrome(12021)
