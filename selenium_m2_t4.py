from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    print(x)

    ans = math.log(abs(12*math.sin(int(x))))
    print(ans)

    ans_element = browser.find_element_by_id('answer')
    ans_element.send_keys(str(ans))

    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()

    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    submit = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()