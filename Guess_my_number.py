''' Угадай число!!! '''
'''
Вы победили с первой попытки!           You won on the first try!
Для Вас суперприз! 1000000 долларов!    Super prize for you! 1000000 dollars!
Сделайте исходную ставку, которая при выигрыше на нечетном ходу удвоится, а на четном - утроится.
Place your original bet, which will double if you win on an odd move and triple on an even one.
Внимание! Если Ваш выигрышный ход окажется простым числом (но не 1)- вся ставка идет мне!!!
Attention! If your winning move turns out to be a prime number (but not 1) - the whole bet goes to me!!!
Сумма Вашего выигрыша...                The amount of your winnings...
'''
import random

game = True
while game:  # while True , но тогда не получится выйти исходя из того, что мы уже умеем
    guess_number = 0
    secret_number = random.randint(1, 20)  # 10
    count_of_try = 0
    # ------------------------------------------------------------------------
    original_bet = float(input("Place your original bet, which will double if you win on an "
                               "odd move and triple on an even one : "))
    print("Attention! If your winning move turns out to be a prime number (but not 1) - the whole bet goes to me!!!")
    # ------------------------------------------------------------------------
    while secret_number != guess_number:
        guess_number = int(input("Enter secret number in range [1-20] : "))
        if secret_number > guess_number:
            print('Your number less than secret')
        elif secret_number < guess_number:
            print('Your number greater than secret')
        count_of_try = count_of_try + 1
    print(f'You win! Your count of tryies {count_of_try} Secret number is {secret_number}')
    # ------------------------------------------------------------------------
    # Accrual of a bonus of $ 1,000,000 for guessing the first time.
    # (Начисление бонуса в 1000000 долларов за угадывание с первого раза.)
    if count_of_try == 1:
        print("You won on the first try!\nSuper prize for you! 1000000 dollars!")
        original_bet = original_bet + 1000000
    # ------------------------------------------------------------------------
    if count_of_try % 2 != 0:  # odd - нечет
        original_bet = 2 * original_bet
    else:
        original_bet = 3 * original_bet

    # Prime number -----------------------------------------------------------
    prime = True # Переключатель ("Ромашка"-простое-непростое-простое-непростое...)
    i = 2  # Prime half counter (Счетчик чисел до половины нашего числа)
    while i <= int((count_of_try / 2) + 1):
        if (count_of_try % i) == 0:
            prime = False
            break
        i = i + 1
    if prime:
            print("Your winning move turns out to be a prime number - the whole bet goes to me!!!")
            original_bet = 0
    # ------------------------------------------------------------------------

    print(f'The amount of your winnings... {original_bet}.')
    # ---
    game = str(input("Press [any key] + [enter] to continue \n or press [enter] to exit :"))
