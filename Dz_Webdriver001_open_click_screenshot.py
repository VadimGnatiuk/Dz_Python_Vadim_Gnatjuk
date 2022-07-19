'''
17_07_22_Webdriver.
Домашнее задание 20
На основании того, что проходили на паре по Selenium WebDriver,
написать программу которая заходит на выбранный заранее сайт,
нажимает на различные элементы меню данного сайта, с переходом на дополнительные страницы
и делает снимки экрана данных страниц ( не менее 10 разных страниц).
Прислать проект в .zip архиве.
'''
# Используем get; button_find по Full Xpath'y; button_click; screenshot
# Variant-1
from selenium import webdriver
import time

site = "https://krijanovka-nvk.odessaedu.net/uk"
driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()

driver.get(site)
time.sleep(3)
driver.get_screenshot_as_file(f'site0.png')

# Нажатие кнопки главного меню "Новости" (# Pressing the main menu button "News")

xpath_button_news = "/html/body/div/div[2]/div/div/ul/li[2]/a"
button_news = driver.find_element("xpath", xpath_button_news)
button_news.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site1.png')

# Нажатие кнопки главного меню "Навчальний процес" (# Pressing the main menu button "Learning process")

xpath_button_learning_process = '/html/body/div/div[2]/div/div/ul/li[3]/a'
button__learning_process = driver.find_element("xpath", xpath_button_learning_process)
button__learning_process.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site2.png')

# Нажатие кнопки главного меню "Інформація для учнів" (# Pressing the main menu button "Information for students")

xpath_button_information_for_students = '/html/body/div/div[2]/div/div/ul/li[4]/a'
button_information_for_students = driver.find_element("xpath", xpath_button_information_for_students)
button_information_for_students.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site3.png')

# Нажатие кнопки главного меню "Вступ до школи" (# Pressing the main menu button "Enter to school")

xpath_button_enter_to_school = '/html/body/div/div[2]/div/div/ul/li[5]/a'
button_enter_to_school = driver.find_element("xpath", xpath_button_enter_to_school)
button_enter_to_school.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site4.png')

# Нажатие кнопки главного меню "Інформація для батьків" (# Pressing the main menu button "Information for Parents")

xpath_button_information_for_parents = '/html/body/div/div[2]/div/div/ul/li[6]/a'
button_information_for_parents = driver.find_element("xpath", xpath_button_information_for_parents)
button_information_for_parents.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site5.png')

# Нажатие кнопки главного меню "Бібліотека" (# Pressing the button of the main menu "Library")

xpath_button_library = '/html/body/div/div[2]/div/div/ul/li[7]/a'
button_library = driver.find_element("xpath", xpath_button_library)
button_library.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site6.png')
# ---------------------------------------------------------------------------------------
# Нажатие кнопки бокового меню "Наша школа" (# Pressing the "Our school" side menu button)

xpath_button_our_school = '/html/body/div/div[3]/div[3]/div[3]/div[2]/div/a'
button_our_school = driver.find_element("xpath", xpath_button_our_school)
button_our_school.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site7.png')

# Нажатие кнопки бокового меню "Наша школа_Як_нас_знайти" (# Pressing the side menu button "Our school_How_to_know_us")

xpath_button_our_school_how_to_know_us = '/html/body/div/div[3]/div[3]/div[4]/div/div[1]/a'
button_our_school_how_to_know_us = driver.find_element("xpath", xpath_button_our_school_how_to_know_us)
button_our_school_how_to_know_us.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site8.png')

# Нажатие кнопки бокового меню "Наша школа_Історія_школи" (# Pressing the side menu button "Our School_History_School")

xpath_button_our_school_history_school = '/html/body/div/div[3]/div[3]/div[4]/div/div[2]/a'
button_our_school_history_school = driver.find_element("xpath", xpath_button_our_school_history_school)
button_our_school_history_school.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site9.png')

# Нажатие кнопки бокового меню "Наша школа_Наші_досягнення"
# (# Pressing the side menu button "Our School_Our_Achievement")

xpath_button_our_school_our_achievement = '/html/body/div/div[3]/div[3]/div[4]/div/div[3]/a'
button_our_school_our_achievement = driver.find_element("xpath", xpath_button_our_school_our_achievement)
button_our_school_our_achievement.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site10.png')

driver.minimize_window()
