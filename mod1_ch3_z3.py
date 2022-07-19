'''
Задание 3
Пользователь вводит с клавиатуры количество метров.
Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили.
'''
# Введите значение длинны, выраженное в метрах:
# В таком случае длинна в *** м, соотвествует *** см, *** дм, *** мм и ** милям.
# Enter a length value expressed in meters:
# In this case, the length is in *** m, corresponding to *** cm, *** dm, *** mm and ** miles.
perem_len = float(input("Enter a length value expressed in meters : "))
print(f'In this case, the length is in {perem_len} m, corresponding to {perem_len * 100} cm, '
      f'{perem_len * 10} dm, {perem_len * 1000} mm and {perem_len / 1609} miles.')

