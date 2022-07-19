'''
Домашнее задание
Закончить программу, которая проходит тест на сайте mensa.
Программа должна брать ответы из файла
'''

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

# Variant-1
'''
Ваоиант-1 это упрощенный вариант, при котором правильные ответы и пути (xpath) к ним 
берутся из готовых файлов ("answer_options.txt" и "xpath_question_minim.txt", соответственно).
'''
# Вопросы с 1 по 8 требуют ввода данных в поле, по-этому будем использовать send_keys()
xpath_file = open('xpath_question_minim.txt', 'rt')  # файл с "путями" к вариантам ответов.
answ_option = open('answer_options.txt', 'rt')  # файл с вариантами ответов.
for i in range(1, 9):
    answer = driver.find_element('xpath', xpath_file.readline()[:-1])
    answer.send_keys(answ_option.readline()[:-1])# Берем соответствующий ответ из "answer_options.txt".
    time.sleep(1)
# --- радиобаттоны и чекбоксы требуют только нажатия на элемент (click()) -----------------------------
for i in range(9, 39):
    answer = driver.find_element('xpath', xpath_file.readline()[:-1])
    answer.click()
    time.sleep(1)
answ_option.close()
xpath_file.close()
# -----------------------------------------------------------------------------------------------------
driver.minimize_window()

# Вывод результата
print(driver.execute_script("return document.IQtest.Result.value"))
