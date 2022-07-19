# Домашнее задание 2; Гнатюк Вадим; Gnatjuk Vadim
# Создать программу которая при вводе данных в переменную метр преобразует его в фут, дюйм, милю и
# литр в пинту, галлон, баррель.
# С использованием данных результатов написать программу, которая выводит текст, по аналогии с тем, как делали на паре.
#
#
# Введите значение длинны           в формате с десятичной точкой
# Указанное вами значение, равное *** метрам, соответствует /// футам, --- дюймам и ___ милям.
# Введите значение емкости
# Указанное вами значение, равное *** литрам, соответствует /// пинтам, --- галлонам и ___ баррелям.

# Enter a length value              in decimal point format
# The value you specify, which is *** meters, corresponds to /// feet, --- inches, and ___ miles.
# Enter capacity value
# The value you entered of *** liters corresponds to /// pints, --- gallons, and ___ barrels.

leng = float(input('Enter a length value (in decimal point format): '))
print(f'The value you specify, which is {leng} meters, corresponds to {leng*3.281} feet, {leng*39.37} inches, and {leng/1609} miles.')

cpcity = float(input('Enter capacity value (in decimal point format): '))
print(f'The value you entered of {cpcity} liters corresponds '
      f'to {cpcity/2.113} pints, {cpcity/3.785} am.gallons, and {cpcity/159} barrels.')
# Как округлять значения