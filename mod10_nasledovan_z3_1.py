'''
Задание 3
Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.)
и поле для хранения копеек (центы, евроценты, копейки и т.д.).
Реализовать методы для вывода суммы на экран, задания значений для частей.
'''
'''
Task 3
Program the Money class (the class object operates with one currency) to work with money.
The classroom should have a field for storing the whole part of the money (dollars, euros, hryvnias, etc.)
and a field for storing kopecks (cents, euro cents, kopecks, etc.).
Implement methods for displaying the sum on the screen, setting values for the parts.
Монеты                  coins
Купюры                  Banknotes
Владелец счёта          Account owner           Money
'''


# Вариант-2, при котором я усложнил задачу. Есть моё видео по её решению.

class Coins:
    number_of_coins = 47
    operation_counter_1 = 0
    sum_add = 0
    sum_stc = 0

    def show_number_of_coins(self):
        return self.number_of_coins

    def add_coins(self, add_coins):
        # self.sum_add = 0
        self.number_of_coins = self.number_of_coins + add_coins  # Сложим монетки вместе.
        if self.number_of_coins >= 100:
            self.sum_add = 1
            self.number_of_coins = self.number_of_coins - 100
            # print(f'sum = {self.sum_add}')
            # print(f'coins = {self.number_of_coins}')
        self.operation_counter_1 = self.operation_counter_1 + 1

    def subtraction_coins(self, subtract_coin):  # Вычитаем монетки из счета.
        # self.sum_stc = 0
        self.number_of_coins = self.number_of_coins - subtract_coin
        if self.number_of_coins <= 0:
            self.sum_stc = -1
            self.number_of_coins = 100 + self.number_of_coins
            #print(f'sum = {self.sum_stc}')
            #print(f'coins = {self.number_of_coins}')
        self.operation_counter_1 = self.operation_counter_1 + 1


class Banknotes:
    number_of_banknotes = 30
    operation_counter_2 = 0
    sum_add = Coins.sum_add
    sum_stc = Coins.sum_stc

    def show_number_of_banknotes(self):
        return self.number_of_banknotes

    def add_banknotes(self, add_banknote):
        self.number_of_banknotes = self.number_of_banknotes + add_banknote + self.sum_add  # Сложим купюры вместе.
        # print(f'number_of_banknotes = {self.number_of_banknotes}')
        self.operation_counter_2 = self.operation_counter_2 + 1

    def subtraction_banknotes(self, subtract_banknotes):  # Вычитаем монетки из счета.
        if self.number_of_banknotes < subtract_banknotes:
            print(f'Sorry, but the amount of banknotes on the account does not allow this operation.\n\t '
                  f'First top up your account with... {subtract_banknotes - self.number_of_banknotes} banknotes.')
        else:
            # print(f'sum_stc = {self.sum_stc}')
            self.number_of_banknotes = self.number_of_banknotes - subtract_banknotes + self.sum_stc
            # print(f'banknotes = {self.number_of_banknotes}')
        self.operation_counter_2 = self.operation_counter_2 + 1


class Account_owner(Coins, Banknotes):
    name = 'Valery'
    operation_counter = 0
    type_of_operation = False  # False - будем снимать со счета, True - ложить на счет.

    def __init__(self, name):
        self.name = name

    def show_your_account_status(self):
        print('* * * * * * * * *  ' * 2)
        print(f'Hello, {self.name}. Your account status : ')
        print(f'{self.show_number_of_banknotes()} banknotes and {self.show_number_of_coins()} coins.')
        print('* * * * * * * * *  ' * 2)

    def adding_money_to_the_account(self, add_banknote, add_coins):  # положить деньги на счет
        self.add_coins(add_coins)
        self.add_banknotes(add_banknote)

    def withdrawal_of_money_from_the_account(self, stc_banknote, stc_coins):  # снять деньги со счета
        self.subtraction_coins(stc_coins)
        self.subtraction_banknotes(stc_banknote)
        self.show_your_account_status()


# coins1 = Coins()
# coins1.show_number_of_coins()
# coins1.add_coins(99)
# print('+++' * 9)
# coins1.show_number_of_coins()
# print('___' * 9)
# coins1.subtraction_coins(86)
# coins1.show_number_of_coins()
#
# print('***' * 9)
# coins2 = Banknotes()
# coins2.show_number_of_banknotes()
# coins2.add_banknotes(50)
# print('***' * 9)
# coins2.show_number_of_banknotes()
# print('***' * 9)
# coins2.subtraction_banknotes(90)
# print('---' * 30)
# coins2.subtraction_banknotes(75)

human = Account_owner("Andrey")
human.show_your_account_status()

human.adding_money_to_the_account(17, 99)
human.show_your_account_status()

human.withdrawal_of_money_from_the_account(30, 50)
# print('sum_add = ', human.sum_add)
# print('sum_str = ', human.sum_stc)
