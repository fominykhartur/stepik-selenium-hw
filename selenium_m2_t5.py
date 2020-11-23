from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os 

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 't.txt')           # добавляем к этому пути имя файла 

path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('1')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('1')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('1')
    input4 = browser.find_element_by_name('file')
    input4.send_keys(file_path)

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()