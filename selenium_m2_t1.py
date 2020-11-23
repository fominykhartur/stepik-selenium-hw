from selenium import webdriver
import time
import math

path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    print(x)
    ans = str(math.log(abs(12*math.sin(int(x)))))

    ans_element = browser.find_element_by_id('answer')
    ans_element.send_keys(ans)

    robot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot.click()

    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()