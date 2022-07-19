'''
Задание 1
Есть множество, содержащее название стран.
Необходимо предоставить пользователю возможности:
1. Добавление стран;
2. Удаления стран;
3. Поиска стран по введенным символам;
4. Проверки существует ли страна внутри множества.
'''

'''
1. Adding countries;
2. Deleting countries;
3. Search for countries by entered characters;
4. Checking whether a country exists within the set.
Новое множество названий стран имеет вид:       The new set of country names looks like:
Ещё раз?        Again?
Среди всех стран, входящих в множество, на ... есть такие:
Among all the countries included in the set, on ... there are:
Введите часть названия страны для поиска:       Enter part of country name for search:
Такая страна есть во множестве.                 There are many such countries.
Такой страны в данном множестве нет.            There is no such country in this set.
'''
country_set = {'Ukraine', 'Australia', 'AAAA', 'The Bahamas', 'Canada', 'AAA', 'Ireland', 'Jamaica', 'New Zealand'}
command = True
while command:
    print(f'Enter your command:\n[a] - for adding countries;\n[d] - for deleting countries;\n[s] - for search for '
          f'countries by entered characters;\n[c] - for checking whether a country exists within the set.\n Or press '
          f'Enter for exit.')
    print(" ___ " * 12)
    command = str(input("??? "))

    if command == 'a':  # adding
        x = str(input(f"Enter country for adding: "))
        set.add(country_set, x)
        print(f'The new set of country names looks like:\n{country_set}.')
        print("___" * 20)
    elif command == 'd':  # 2.----------------------------------------------------
        x = str(input(f"Enter country for deleting: "))
        set.remove(country_set, x)
        print(f'The new set of country names looks like:\n{country_set}.')
        print("+++" * 20)
    elif command == 's':  # 3.----------------------------------------------------
        x = str(input(f"Enter part of country name for search: "))
        print(f'Among all the countries included in the set, on {x} there are:')
        for elem in country_set:
            if x in elem:
                print(elem)
    elif command == 'c':  # 4.----------------------------------------------------
        x = str(input(f"Enter country for checking whether a country: "))
        if x in country_set:  # среди элементов множества есть ВВЕДЕННЫЙ или нет?
            print("There are many such countries.")
            print(f'The set of country names looks like:\n{country_set}.')
            print("===" * 20)
        else:
            print("There is no such country in this set.")
            print(f'The set of country names looks like:\n{country_set}.')
            print("===" * 20)
    else:
        print("Good bay.")
