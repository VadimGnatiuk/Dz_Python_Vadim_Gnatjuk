'''
Задание 2
Создайте класс Ship, который содержит информацию о корабле.
С помощью механизма наследования, реализуйте
класс Frigate (содержит информацию о фрегате),
класс Destroyer (содержит информацию об эсминце),
класс Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые для работы методы.
'''


class Ship:
    name = 'Nautilus'
    sail = 'Jolly Roger'
    year_of_launch = 1975

    def show_name(self):
        print(self.name)

    def change_name(self, new_name):
        self.name = new_name

    def show_sail(self):
        print(self.sail)

    def change_sail(self, new_sail):
        self.sail = new_sail

    def show_year_of_launch(self):
        print(self.year_of_launch)

    def change_year_of_launch(self, new_year_of_launch):
        self.year_of_launch = new_year_of_launch

    def show_all_fields(self):
        print(f'name = {self.name}')
        print(f'sail = {self.sail}')
        print(f'year_of_launch = {self.year_of_launch}')


class Frigate(Ship):
    ship_type = 'Frigate'
    fleet_to_lie_down = 'Black Sea'

    def show_ship_type(self):
        print(self.ship_type)

    def change_ship_type(self, new_ship_type):
        self.ship_type = new_ship_type

    def show_fleet_to_lie_down(self):
        print(self.fleet_to_lie_down)

    def change_fleet_to_lie_down(self, new_fleet_to_lie_down):
        self.fleet_to_lie_down = new_fleet_to_lie_down


class Destroyer(Ship):
    ship_type = 'Destroyer'
    fleet_to_lie_down = 'Atlantic Fleet'
    the_number_of_mines_that_can_set = 100

    def show_ship_type(self):
        print(self.ship_type)

    def change_ship_type(self, new_ship_type):
        self.ship_type = new_ship_type

    def show_fleet_to_lie_down(self):
        print(self.fleet_to_lie_down)

    def change_fleet_to_lie_down(self, new_fleet_to_lie_down):
        self.fleet_to_lie_down = new_fleet_to_lie_down

    def show_the_number_of_mines_that_can_set(self):
        print(self.the_number_of_mines_that_can_set)

    def change_the_number_of_mines_that_can_set(self, new_the_number_of_mines_that_can_set):
        self.the_number_of_mines_that_can_set = new_the_number_of_mines_that_can_set


class Cruiser(Ship):
    ship_type = 'Cruiser'
    fleet_to_lie_down = 'Arctic Ocean'
    armor_thickness = 1.2  # Для крейсера сменим поле "количество мин" на "толщину брони".
    name = 'Proud'  # Попробуем СХОДУ перееопределить имя крейсера, а не наследовать его из класса "Ship".

    def show_ship_type(self):
        print(self.ship_type)

    def change_ship_type(self, new_ship_type):
        self.ship_type = new_ship_type

    def show_fleet_to_lie_down(self):
        print(self.fleet_to_lie_down)

    def change_fleet_to_lie_down(self, new_fleet_to_lie_down):
        self.fleet_to_lie_down = new_fleet_to_lie_down

    def show_armor_thickness(self):
        print(self.armor_thickness)

    def change_armor_thickness(self, new_armor_thickness):
        self.armor_thickness = new_armor_thickness


print('___' * 12)
ship1 = Ship()
ship1.show_all_fields()
print('___' * 12)

print('___' * 12)
ship2 = Frigate()
ship2.show_all_fields()
ship2.change_year_of_launch(2000)
print('___' * 12)
# print(ship2.year_of_launch)
ship2.show_year_of_launch()
print('___' * 12)
ship2.show_ship_type()
ship2.show_fleet_to_lie_down()
print('___' * 12)

print('===' * 12)
ship3 = Destroyer()
ship3.show_all_fields()
print('===' * 12)
ship3.show_ship_type()
ship3.show_fleet_to_lie_down()
ship3.show_the_number_of_mines_that_can_set()
print('===' * 12)
ship3.change_name('Swift')
ship3.show_name()
ship3.change_the_number_of_mines_that_can_set(500)
ship3.show_the_number_of_mines_that_can_set()
print('===' * 12)

print('***' * 12)
ship3 = Cruiser()
ship3.show_all_fields()
print('***' * 12)
ship3.show_ship_type()
ship3.show_fleet_to_lie_down()
ship3.show_armor_thickness()
print('***' * 12)
#ship3.change_name('Swift')
#ship3.show_name()
ship3.change_armor_thickness(1.5)
ship3.show_armor_thickness()
print('***' * 12)

