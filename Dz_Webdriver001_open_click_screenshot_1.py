'''
17_07_22_Webdriver.
Домашнее задание 20
На основании того, что проходили на паре по Selenium WebDriver,
написать программу которая заходит на выбранный заранее сайт,
нажимает на различные элементы меню данного сайта, с переходом на дополнительные страницы
и делает снимки экрана данных страниц ( не менее 10 разных страниц).
Прислать проект в .zip архиве.
'''
# Используем get; button_find по Full Xpath'y; button_click; screenshot; loop_for
# Variant-2
from selenium import webdriver
import time

site = "https://krijanovka-nvk.odessaedu.net/uk"
driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()

driver.get(site)
time.sleep(3)
driver.get_screenshot_as_file(f'site0.png')

# Нажатие кнопок главного меню (# Pressing the main menu button)

for count in range(2, 7 + 1):
    xpath_button = f'/html/body/div/div[2]/div/div/ul/li[{count}]/a'
    button = driver.find_element("xpath", xpath_button)
    button.click()
    time.sleep(3)
    driver.get_screenshot_as_file(f'site{count - 1}.png')

# ---------------------------------------------------------------------------------------
# Нажатие кнопки бокового меню "Наша школа" (# Pressing the "Our school" side menu button)

xpath_button_our_school = '/html/body/div/div[3]/div[3]/div[3]/div[2]/div/a'
button_our_school = driver.find_element("xpath", xpath_button_our_school)
button_our_school.click()
time.sleep(3)
driver.get_screenshot_as_file(f'site7.png')

# Нажатие кнопки бокового меню "Наша школа_1_3" (# Pressing the side menu button "Our school_1_3")

for count in range(1, 4):
    xpath_button_our_school = f'/html/body/div/div[3]/div[3]/div[4]/div/div[{count}]/a'
    button_our_school = driver.find_element("xpath", xpath_button_our_school)
    button_our_school.click()
    time.sleep(3)
    driver.get_screenshot_as_file(f'site{count + 7}.png')

driver.minimize_window()
