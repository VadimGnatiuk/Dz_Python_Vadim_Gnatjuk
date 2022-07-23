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
'''


class Money:
    banknotes = 47
    coins = 99

    def show_sum(self):
        print(f'Your account status :\n\t {self.banknotes} banknotes and {self.coins} coins.')

    def change_banknotes(self, enter_banknotes):
        self.banknotes = self.banknotes + enter_banknotes

    def change_coins(self, enter_coins):
        self.coins = self.coins + enter_coins
        if self.coins >= 100:
            self.banknotes = self.banknotes + 1
            self.coins = self.coins - 100


print('+++' * 12)
people1 = Money()
people1.show_sum()
print('+++' * 12)
people1.change_banknotes(100)
people1.change_coins(50)
people1.show_sum()
print('+++' * 12)

