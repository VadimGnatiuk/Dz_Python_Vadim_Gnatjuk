'''
Домашнее задание
В файле .py, написать переменные с XPATH,
всех ответов и их вариантов с сайта

https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html

xpath_question1_entry = '//input[@name="q1"]'
xpath_question9_radio_b = '//input[@name="q9"][@value="b"]'
# '//input[@name="q9" and @value="b"]'
#//img[@src="/images/site/iq21a.gif"]
Файл .py прислать в MyStat
'''
'''
всех ответов и их вариантов с сайта     
all answers and their options from the site
'''
# Variant-2
for ans_1_8 in range(1, 9):
    xpath_answer_1_8 = f'//input[@name="q{ans_1_8}"]'
    print(f'xpath_answer_{ans_1_8} = ', xpath_answer_1_8)
print()

letter_answers = 'abcd'
letter_answers1 = 'abcde'

for ans_9_18 in range(9, 19):
    for i in letter_answers:
        xpath_answer_9_18_i = f'//input[@name="q{ans_9_18}"][@value="{i}"]'
        print(f'xpath_answer_{ans_9_18}_{i} = ', xpath_answer_9_18_i)
print()

for ans_19_22 in range(19, 23):
    for i in letter_answers1:
        xpath_answer_19_22_i = f'//input[@name="q{ans_19_22}"][@value="{i}"]'
        print(f'xpath_answer_{ans_19_22}_{i} = ', xpath_answer_19_22_i)
print()

for ans_23_33 in range(23, 34):
    for i in letter_answers:
        xpath_answer_23_33_i = f'//input[@name="q{ans_23_33}"][@value="{i}"]'
        print(f'xpath_answer_{ans_23_33}_{i} = ', xpath_answer_23_33_i)
print()

xpath_finished = '//input[@value="FINISHED"]'
print('xpath_finished = ', xpath_finished)
