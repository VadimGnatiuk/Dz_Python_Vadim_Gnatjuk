'''
Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя,
цвет машины, цену. Реализуйте методы класса для ввода данных,
вывода данных, реализуйте доступ к отдельным полям через методы класса.'''

'''Exercise 1
Implement the Car class. Must be stored in class fields:
model name, year of manufacture, manufacturer, engine size,
car color, price. Implement class methods for data entry,
data output, implement access to individual fields through class methods.
'''


class Car:
    model_name = 'toyota'
    year_of_manufacture = 2020
    manufacturer = 'Japan'
    engine_size = '2 l'
    car_color = 'black'
    price = 150000

    # Метод __init__ существует и сам по себе, по умолчанию, но его можно ПЕРЕопределять,
    # например, если я хочу выбрать некоторые поля (аргументы, атрибуты) данного класса ОБЯЗАТЕЛЬНЫМИ
    # (???) или добавить в класс нечто новое(???)

    def __init__(self, model_name, year_of_manufacture, price):
        self.model_name = model_name
        self.year_of_manufacture = year_of_manufacture
        self.price = price

    def show_model_name(self):
        print(self.model_name)

    def change_model_name(self, new_model_name):
        self.model_name = new_model_name

    def show_year_of_manufacture(self):
        print(self.year_of_manufacture)

    def change_year_of_manufacture(self, new_year_of_manufacture):
        self.year_of_manufacture = new_year_of_manufacture

    def show_manufacturer(self):
        print(self.manufacturer)

    def change_manufacturer(self, new_manufacturer):
        self.manufacturer = new_manufacturer

    def show_engine_size(self):
        print(self.engine_size)

    def change_engine_size(self, new_engine_size):
        self.engine_size = new_engine_size

    def show_car_color(self):
        print(self.car_color)

    def change_car_color(self, new_car_color):
        self.car_color = new_car_color

    def show_price(self):
        print(self.price)

    def change_price(self, new_price):
        self.price = new_price

    def show_all_fields(self):
        print(f'model_name = {self.model_name}')
        print(f'year_of_manufacture = {self.year_of_manufacture}')
        print(f'manufacturer = {self.manufacturer}')
        print(f'engine_size = {self.engine_size}')
        print(f'car_color = {self.car_color}')
        print(f'price = {self.price}')


# Обратить внимание! После добавления метода __init__ (с тремя параметрами)
# команда ниже (car1 = Car()), которая определяет (создает) переменную класса Car() с именем "car1", начинает
# "ругаться" (выделает скобку) - требует ввести эти самые параметры.
car1 = Car('BMW', '1975', 1000000)
car1.show_model_name()
car1.change_model_name('ford')
car1.show_model_name()
print('___' * 9)

car2 = Car('opel', '2000', 50000)
car2.show_year_of_manufacture()
car2.change_year_of_manufacture(2005)
car2.show_year_of_manufacture()
print('___' * 9)

car3 = Car('renault', '2010', 5000)
car3.show_manufacturer()
car3.change_manufacturer('France')
car3.show_manufacturer()
print('___' * 9)

car4 = Car('Peugeot', '2015', 7000)
car4.show_engine_size()
car4.change_engine_size('0.5 l')
car4.show_engine_size()
print('___' * 9)

car5 = Car('Hyundai', '2010', 5000)
car5.show_car_color()
car5.change_car_color('White')
car5.show_car_color()
print('___' * 9)

car6 = Car('Волга', '2010', 5000)
car6.show_price()
car6.change_price(500)
car6.show_price()
print('___' * 9)

car7 = Car('Tesla', '2022', 1000000000)
car7.show_all_fields()
