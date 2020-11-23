from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    x_element = browser.find_element_by_css_selector('h2 #num1')
    x = x_element.text
    print(x)
    y_element = browser.find_element_by_css_selector('h2 #num2')
    y = y_element.text
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))

    select.select_by_value(str(int(x)+int(y))) 

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()