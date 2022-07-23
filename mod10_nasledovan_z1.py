'''
Задание 1
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте
класс CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере),
класс MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые для работы методы.
'''


class Device:
    manufacturing_firm = ' OOO "Alpha" '
    color = 'black'
    max_power = 220
    producing_country = 'Ukraine'

    def show_manufacturing_firm(self):
        print(self.manufacturing_firm)

    def change_manufacturing_firm(self, new_manufacturing_firm):
        self.manufacturing_firm = new_manufacturing_firm

    def show_color(self):
        print(self.color)

    def change_color(self, new_color):
        self.color = new_color

    def show_max_power(self):
        print(self.max_power)

    def change_max_power(self, new_max_power):
        self.max_power = new_max_power

    def show_producing_country(self):
        print(self.producing_country)

    def change_producing_country(self, new_producing_country):
        self.producing_country = new_producing_country

    def show_all_class_fields(self):
        print(f'manufacturing_firm : {self.manufacturing_firm}')
        print(f'color : {self.color}')
        print(f'max_power : {self.max_power}')
        print(f'producing_country : {self.producing_country}')


# --- Checked the operation of all argument fields ------------------------------------------------
# --- Проверили работу всех полей-аргументов ---
device1 = Device()

print(device1.manufacturing_firm)
device1.change_manufacturing_firm('Gonduras')
print(device1.manufacturing_firm)

print(device1.color)
device1.change_color('white')
print(device1.color)

print(device1.max_power)  # Можно выводить принтом значение поля (через функцию), а можно
device1.change_max_power('110')
device1.show_max_power()  # через метод (если те его создал, конечно).

print(device1.producing_country)
device1.change_producing_country('Poland')
device1.show_producing_country()

device1.show_all_class_fields()


# -------------------------------------------------------------------------------------------------
# Создам подклассы "кофемолка", "мясорубка" и т.д. у каждого из них будет свое поле "цена" и сделаю
# метод "использование устройства(амортизация)" в котором буду уменьшать стоимость
# устройства на 10% после каждого использования.

class CoffeeMachine(Device):
    price = 10000

    def show_price(self):
        print(self.price)

    def change_price(self, new_price):  # Это - возможность поменять цену аппарата (при покупке...)
        self.price = new_price

    def device_depreciation(self, percent):
        print("worked a little...")
        self.price = (self.price * (100 - percent)) / 100


class Blender(Device):
    price = 7500

    def show_price(self):
        print(self.price)

    def change_price(self, new_price):
        self.price = new_price

    def device_depreciation(self, percent):
        print("worked a little...")
        self.price = (self.price * (100 - percent)) / 100


class MeatGrinder(Device):
    price = 7500

    def show_price(self):
        print(self.price)

    def change_price(self, new_price):
        self.price = new_price

    def device_depreciation(self, percent):
        print("worked a little...")
        self.price = (self.price * (100 - percent)) / 100


device_coffee = CoffeeMachine()
print('___' * 12)
device_coffee.show_all_class_fields()
print('___' * 12)
device_coffee.show_price()
device_coffee.change_price(5000)
device_coffee.show_price()
print('___' * 12)
device_coffee.device_depreciation(10)
device_coffee.show_price()

device_blender = Blender()
print('+++' * 12)
device_blender.show_all_class_fields()
print('+++' * 12)
device_blender.show_price()
device_blender.change_price(5000)
device_blender.show_price()
print('+++' * 12)
device_blender.device_depreciation(5)
device_blender.show_price()

device_meatgrinder = MeatGrinder()
print('_ _' * 12)
device_meatgrinder.show_all_class_fields()
print('_ _' * 12)
device_meatgrinder.show_price()
device_meatgrinder.change_price(3000)
device_meatgrinder.show_price()
print('_ _' * 12)
device_meatgrinder.device_depreciation(30)
device_meatgrinder.show_price()
