'''
Задание 2
Реализуйте класс «Книга». Необходимо хранить в полях класса:
название книги, год выпуска, издателя, жанр, автора, цену.
Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
'''
'''
Task 2
Implement the Book class. Must be stored in class fields:
title of the book, year of release, publisher, genre, author, price.
Implement class methods for data input, data output,
implement access to individual fields through class methods.
'''


# Упрощенный вариант (без переопределения метода __init__).

class Book:
    title_of_the_book = 'Interceptor'
    year_of_release = 1995
    publisher = 'Lion-book'
    genre = 'fantasy'
    author = 'Vasily Golovachev'
    price = 3000

    def show_title_of_the_book(self):
        print(self.title_of_the_book)

    def change_title_of_the_book(self, new_title_of_the_book):
        self.title_of_the_book = new_title_of_the_book

    def show_year_of_release(self):
        print(self.year_of_release)

    def change_year_of_release(self, new_year_of_release):
        self.year_of_release = new_year_of_release

    def show_publisher(self):
        print(self.publisher)

    def change_publisher(self, new_publisher):
        self.publisher = new_publisher

    def show_genre(self):
        print(self.genre)

    def change_genre(self, new_genre):
        self.genre = new_genre

    def show_author(self):
        print(self.author)

    def change_author(self, new_author):
        self.author = new_author

    def show_price(self):
        print(self.price)

    def change_price(self, new_price):
        self.price = new_price

    def show_all_fields(self):
        print(f'title_of_the_book = {self.title_of_the_book}')
        print(f'year_of_release = {self.year_of_release}')
        print(f'publisher = {self.publisher}')
        print(f'genre = {self.genre}')
        print(f'author = {self.author}')
        print(f'price = {self.price}')


print('---' * 9)
book1 = Book()
book1.show_title_of_the_book()
print('---' * 9)
book2 = Book()
book2.show_year_of_release()
print('---' * 9)
book3 = Book()
book3.show_publisher()
print('---' * 9)
book4 = Book()
book4.show_genre()
print('---' * 9)
book5 = Book()
book5.show_author()
print('---' * 9)
book6 = Book()
book6.show_price()
print('---' * 9)

book1.change_title_of_the_book('Garnet bracelet')
book2.change_year_of_release(1900)
book3.change_publisher('BookMan')
book4.change_genre('detective')
book5.change_author('Agatha Christie')
book6.change_price(123)

# for i in range(1,7):
#     print(f'{i} = ',book{i}.show_all_fields())

book1.show_all_fields()
