from selenium import webdriver
import time
import math

path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    print(x)
    ans = str(math.log(abs(12*math.sin(int(x)))))

    ans_element = browser.find_element_by_id('answer')
    ans_element.send_keys(ans)

    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()