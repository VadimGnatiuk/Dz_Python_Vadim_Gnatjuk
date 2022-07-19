'''
Задание 4
Зарплата менеджера составляет 200$ + процент от продаж,
продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
Пользователь вводит с клавиатуры уровень продаж для трех менеджеров.
Определить их зарплату, определить лучшего менеджера, начислить ему премию
200$, вывести итоги на экран.
'''
'''
1.  Было бы полезным прогнать програму через тест-кейс 
    с полным комплектом тестовых случаев (только его сначала создать надо)
2.  Программу сделано чётко по условию (например, нет обработки условия с двумя одинаковыми и одним наихудшим...)
'''

'''
Укажите уровень продаж первого менеджера:       Specify the level of sales of the first manager:
Укажите уровень продаж второго менеджера:       Specify the sales level of the second manager:
Укажите уровень продаж третьего менеджера:      Specify the level of sales of the third manager:
Зарплата первого менеджера                      First manager salary    *** fms
Зарплата второго менеджера                      Second manager salary   *** sms
Зарплата третьего менеджера                     Third manager salary    *** tms   
Эй-эй! В нашей команде ЖИВЫЕ менеджеры в убыток не работают! Запустите программу снова.

"Уважаемый" менеджер, а Вы работать не пробовали?       "Dear" manager, have you tried to work?
Все менеджеры работали на одном уровне продаж... Молодцы!   All managers worked at the same sales level... Well done!
Итого, за период:               Total for the period: 
Лидер продаж -                  Bestseller -
Подаёт надежды -                Gives hope -
Скоро освободит вакансию -      Will vacate soon -
с суммой -                      with sum -
Явный лидер продаж не обнаружен (минимум двое из Вас показали равный результат)!
No clear bestseller found (at least two of you are tied)!
'''
level_of_sales_1 = float(input("Specify the level of sales of the first manager : "))
level_of_sales_2 = float(input("Specify the sales level of the second manager : "))
level_of_sales_3 = float(input("Specify the level of sales of the third manager : "))
fms = sms = tms = 200  # Salary rate (Ставка зарплаты)
d1 = 0.03  # <500               -> 3%
d2 = 0.05  # >=500 and <= 1000  -> 5%
d3 = 0.08  # >1000              -> 8%
if level_of_sales_1 < 0 or level_of_sales_2 < 0 or level_of_sales_3 < 0:
    print("Hey Hey! In our team, LIVE managers do not work at a loss! Run the program again.")
else:
    if (level_of_sales_1 > 0) and (level_of_sales_1 < 500):
        fms = fms + (fms * d1)
    elif level_of_sales_1 >= 500 and level_of_sales_1 <= 1000:
        fms = fms + fms * d2
    elif level_of_sales_1 > 1000:
        fms = fms + fms * d3
    else:
        print("\"Dear\" manager, have you tried to work?")

    if (level_of_sales_2 > 0) and (level_of_sales_2 < 500):
        sms = sms + (sms * d1)
    elif level_of_sales_2 >= 500 and level_of_sales_2 <= 1000:
        sms = sms + sms * d2
    elif level_of_sales_2 > 1000:
        sms = sms + sms * d3
    else:
        print("\"Dear\" manager, have you tried to work?")

    if (level_of_sales_3 > 0) and (level_of_sales_3 < 500):
        tms = tms + (tms * d1)
    elif level_of_sales_3 >= 500 and level_of_sales_3 <= 1000:
        tms = tms + tms * d2
    elif level_of_sales_3 > 1000:
        tms = tms + tms * d3
    else:
        print("\"Dear\" manager, have you tried to work?")
# Premium accrual (Начисление премии)
    if fms == sms == tms:
        print("All managers worked at the same sales level... Well done!")
    elif (fms > sms) and (sms > tms):
        fms = fms + 200
        print(f'Total for the period:\n'
              f'Bestseller... first manager, with sum - {fms}.\n'
              f'\tGives hope... second manager, with sum - {sms}.\n'
              f'\t\tWill vacate soon... third manager, with sum - {tms}.')
    elif (sms > fms) and (fms > tms):
        sms = sms + 200
        print(f'Total for the period:\n'
              f'Bestseller... second manager, with sum - {sms}.\n'
              f'\tGives hope... first manager, with sum - {fms}.\n'
              f'\t\tWill vacate soon... third manager, with sum - {tms}.')
    elif (tms > sms) and (sms > fms):
        tms = tms + 200
        print(f'Total for the period:\n'
              f'Bestseller... third manager, with sum - {tms}.\n'
              f'\tGives hope... second manager, with sum - {sms}.\n'
              f'\t\tWill vacate soon... first manager, with sum - {fms}.')
    else:
        print("No clear bestseller found (at least two of you are tied)!\n")
        print(f'Total for the period:\n'
              f'First manager, with sum... {fms}.\n'
              f'\tSecond manager, with sum... {sms}.\n'
              f'\t\tThird manager, with sum... {tms}.')

#print(fms, sms, tms)
