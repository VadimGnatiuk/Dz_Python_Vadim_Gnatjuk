'''
Задание 6
В словаре хранится набор пар: Название страны -> Столица.
Нужно реализовать функциональность по добавлению, удалению, поиску и замене.
'''
countries = {'Kyiv': 'Ukraine', 'Warsaw': 'Poland', 'Berlin': 'Germany', 'Paris': 'France', 'Rome': 'Italy'}
command = True
while command:
    command = str(input('Enter command: \n[r] - read\n[c] - create\n[d] - delete\n[s] - search\n[u] - update\n: '))
    if command == 'r':
        #Read
        for capital in countries:
            print(f'Capital : {capital}  \tCountry : {countries[capital]}')
    elif command == 'c':
        #Create
        capital = str(input('Enter capital of country : '))
        country = str(input('Enter country : '))
        countries[capital] = country
    elif command == 'd':
        #Delete
        capital = str(input('Enter capital of country : '))
        del countries[capital]
    elif command == 's':
        capital = str(input(f"Enter capital name for search: "))
        for elem in countries:
            if capital in elem:
                print(f'Capital : {capital}  \tCountry : {countries[capital]}')
    elif command == 'u':
        #Update
        capital = str(input('Enter capital of country : '))
        country = str(input('Enter country : '))
        countries[capital] = country
    else:
        print("Good bay.")