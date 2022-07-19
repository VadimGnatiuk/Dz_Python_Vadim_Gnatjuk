'''
Задание 3
Написать программу подсчета стоимости разговора для разных мобильных операторов.
Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит.
Вывести стоимость на экран.
'''

'''
Укажите время Вашего разговора :        Specify the time of your conversation:    
Укажите мобильного оператора_1          Specify mobile operator_1
Тариф первого оператора                 First operator tariff
Тариф второго оператора                 Second operator tariff
Стоимость разговора =                   Call cost =
Укажите оператора, с которого совершен исходящий звонок     Specify the operator from which the outgoing call was made
Укажите, на телефон какого оператора будет совершен звонок : 
Specify which operator's phone number the call will be made to:
Вы можете звонить бесплатно             You can call for free
Вы должны оплатить сумму :              You must pay the amount:
'''
# Block known variables (Блок известный переменных)
ks_tarif = 0.47     # tariff Kievstar   - 47 cent/min
lc_tarif = 0.30     # tariff lifecell   - 30 cent/min
mts_tarif = 0.52    # tariff MTS        - 52 cent/min

oper_1 = str(input("Specify the operator from which the outgoing call was made - \n[k]ievstar, [l]ifecell, [m]ts : "))
oper_2 = str(input("Specify which operator's phone number the call will be made to - \n[k]ievstar, "
                   "[l]ifecell, [m]ts : "))
call_cost = float(input("Enter call cost : "))
if oper_1 == oper_2:
    print("You can call for free!")
if oper_1 == 'k' and oper_2 == 'l':
    print(f'You must pay the amount: {call_cost/ks_tarif*lc_tarif}.')
if oper_1 == 'k' and oper_2 == 'm':
    print(f'You must pay the amount: {call_cost/ks_tarif*mts_tarif}.')
if oper_1 == 'l' and oper_2 == 'k':
    print(f'You must pay the amount: {call_cost/lc_tarif*ks_tarif}.')
if oper_1 == 'l' and oper_2 == 'm':
    print(f'You must pay the amount: {call_cost/lc_tarif*mts_tarif}.')
if oper_1 == 'm' and oper_2 == 'k':
    print(f'You must pay the amount: {call_cost/mts_tarif*ks_tarif}.')
if oper_1 == 'm' and oper_2 == 'l':
    print(f'You must pay the amount: {call_cost/mts_tarif*lc_tarif}.')

