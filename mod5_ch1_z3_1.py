'''
Задание 3
Напишите функцию, которая отображает пустой или заполненный квадрат
из некоторого символа. Функция принимает в качестве параметров:
длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
'''
# Вариант реализации, когда переключатель (switcher) реализован через ЛОГИЧЕСКУЮ (True/False) переменную:

# switcher = str(input("Enter [T]rue / [F]alse : "))
# symbol = '*'
# length = 5
# space = ' '
# square = ''
def displaying_an_empty_or_filled_square(length, symbol, switcher=False):
    space = ' '
    square = ''
    symb_leng = len(symbol)
    if switcher:
        for i in range(length):
            square = square + length * symbol + '\n'
    else:
        for i in range(length):
            if i == 0 or i == (length - 1):
                square = square + (length * symbol) + '\n'
            else:
                square = square + symbol + ((length - 2) * symb_leng * space) + symbol + '\n'
    print(square)


displaying_an_empty_or_filled_square(3, '||')
displaying_an_empty_or_filled_square(5, '**', True)
displaying_an_empty_or_filled_square(7, '* *')
displaying_an_empty_or_filled_square(8,'+','True')

