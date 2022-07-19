'''
Домашнее задание
Закончить программу, которая проходит тест на сайте mensa.
Программа должна брать ответы из файла'''

# Variant-2
'''Вариант-2 это вариант, в котором для вопросов (9-33) удалось автоматизировать ПОЛНОСТЬЮ так, чтобы
ПК брал правильный вариант ответа из файла "answer_options.txt", подставлял ЭТУ букву
в соответствующий xpath (точнее, выбирал соответствующий ПРАВИЛЬНОМУ варианту xpath) и
на него "кликал".'''

'''
запись _ 1          entry _ 1
ОТВЕТЫ              ANSWERS
вопрос              question
варианты ответов    answer options
Answers             Ответы
'''
from selenium import webdriver
import time

url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(1)

# Модуль 1 - За основу взят проект "Dz_24_07_2022_Webdriver002_xpath_loop_files.py"
# (поиск и сохранение xpass-сов для вопросов и ответов)

f = open('xpath_question.txt', 'wt')
for ans_1_8 in range(1, 9):
    xpath_answer_1_8 = f'//input[@name="q{ans_1_8}"]'
    # f.write(f'xpath_answer_{ans_1_8} = ')
    f.write(xpath_answer_1_8)
    f.write('\n')
# f.write('\n')# Отделяем блок со вводом в поле от блока радиобаттонов.

letter_answers = 'abcd'
letter_answers1 = 'abcde'

for ans_9_18 in range(9, 19):
    for i in letter_answers:
        xpath_answer_9_18_i = f'//input[@name="q{ans_9_18}"][@value="{i}"]'
        # f.write(f'xpath_answer_{ans_9_18}_{i} = ')
        f.write(xpath_answer_9_18_i)
        f.write('\n')
# f.write('\n')# Отделяем блок радиобаттонов от блока чекбоксов.

for ans_19_22 in range(19, 23):
    for i in letter_answers1:
        xpath_answer_19_22_i = f'//input[@name="q{ans_19_22}"][@value="{i}"]'
        # f.write(f'xpath_answer_{ans_19_22}_{i} = ')
        f.write(xpath_answer_19_22_i)
        f.write('\n')
# f.write('\n')# Отделяем блок чекбоксов от блока радиобаттонов.

for ans_23_33 in range(23, 34):
    for i in letter_answers:
        xpath_answer_23_33_i = f'//input[@name="q{ans_23_33}"][@value="{i}"]'
        # f.write(f'xpath_answer_{ans_23_33}_{i} = ')
        f.write(xpath_answer_23_33_i)
        f.write('\n')
# f.write('\n')# Отделяем блок радиобаттонов от кнопки "FINISHED".

xpath_finished = '//input[@value="FINISHED"]'
# f.write('xpath_finished = ')
f.write(xpath_finished)
f.write('\n')
f.close()
# __________________________________________________________________________________
# Вспомогательный ----------------------
# f = open('xpath_question.txt', 'rt')
# print(f.readlines())
# f.close()
# --------------------------------------
# # Create a file with answer options (Создаем файл с вариантами ответов)
# Модуль 2 - создали "пустой" файл для ответов, после чего "ВРУЧНУЮ" внесли в него "ПРАВИЛЬНЫЕ" ответы.
# f = open('answer_options.txt','wt')
# for i in range(8):
#     f.write('a')
#     f.write('\n')
# f.close()

# Модуль 3 --------------------------------------------------------------------------------------------
# Вопросы с 1 по 8 требуют ввода данных в поле, поэтому будем использовать send_keys()
xpath_file = open('xpath_question.txt', 'rt')  # файл с "путями" к вариантам ответов.
answ_option = open('answer_options.txt', 'rt')  # файл с вариантами ответов.
for i in range(1, 9):  # 1-8
    xp = xpath_file.readline()[:-1]
    answer = driver.find_element('xpath', xp)
    answer.send_keys(answ_option.readline()[:-1])
    # time.sleep(1)
    #print(xp)
for i in range(9, 19):  # 9-18
    ao = answ_option.readline()[:-1]
    #print(ao)
    for j in range(4):
        xp = xpath_file.readline()[:-1]
        #print(xp)
        #print(xp[-3:-2])
        if xp[-3:-2] == ao:
            answer = driver.find_element('xpath', xp)
            answer.click()
            # time.sleep(1)
for i in range(19, 23):  # 19-22
    ao = answ_option.readline()[:-1]
    #print(ao)
    for j in range(5):
        xp = xpath_file.readline()[:-1]
        #print(xp)
        #print(xp[-3:-2])
        if xp[-3:-2] == ao[0]:  # В этих четырех ответах ("ао") по ДВЕ буквы правильные!
            answer = driver.find_element('xpath', xp)
            answer.click()
            # time.sleep(1)
        if xp[-3:-2] == ao[1]:  # В этих четырех ответах ("ао") по ДВЕ буквы правильные!
            answer = driver.find_element('xpath', xp)
            answer.click()
            # time.sleep(1)
for i in range(23, 34):  # 23-33
    ao = answ_option.readline()[:-1]
    #print(ao)
    for j in range(4):
        xp = xpath_file.readline()[:-1]
        #print(xp)
        #print(xp[-3:-2])
        if xp[-3:-2] == ao:
            answer = driver.find_element('xpath', xp)
            answer.click()
            # time.sleep(1)
answer = driver.find_element('xpath', xpath_file.readline()[:-1])
answer.click()
time.sleep(1)

answ_option.close()
xpath_file.close()
# -----------------------------------------------------------------------------------------------------
driver.minimize_window()
# Вывод результата
print(driver.execute_script("return document.IQtest.Result.value"))
