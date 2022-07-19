'''
Задание 3
Реализуйте класс «Стадион». Необходимо хранить в полях класса:
название стадиона, дату открытия, страну, город, вместимость.
Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
'''
'''
Task 3
Implement the Stadium class. Must be stored in class fields:
stadium name, opening date, country, city, capacity.
Implement class methods for data input, data output,
implement access to individual fields through class methods.
'''


# Упрощенный вариант (без переопределения метода __init__).
class Stadium:
    stadium_name = 'VikingS'
    opening_date = '01/01/1999'
    country = 'Norway'
    city = 'Oslo'
    capacity = 30000

    def show_stadium_name(self):
        print(self.stadium_name)

    def change_stadium_name(self, new_stadium_name):
        self.stadium_name = new_stadium_name

    def show_opening_date(self):
        print(self.opening_date)

    def change_opening_date(self, new_opening_date):
        self.opening_date = new_opening_date

    def show_country(self):
        print(self.country)

    def change_country(self, new_country):
        self.country = new_country

    def show_city(self):
        print(self.city)

    def change_city(self, new_city):
        self.city = new_city

    def show_capacity(self):
        print(self.capacity)

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity

    def show_all_fields(self):
        print(f'stadium_name = {self.stadium_name}')
        print(f'opening_date = {self.opening_date}')
        print(f'country = {self.country}')
        print(f'city = {self.city}')
        print(f'capacity = {self.capacity}')


print('---' * 9)
stadium1 = Stadium()
stadium1.show_all_fields()
print('---' * 9)
stadium1.change_stadium_name('ORBITA')
stadium1.show_all_fields()
