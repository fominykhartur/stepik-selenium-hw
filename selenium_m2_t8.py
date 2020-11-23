from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    book = browser.find_element_by_id("book")
    book.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    print(x)

    ans = math.log(abs(12*math.sin(int(x))))
    print(ans)

    ans_element = browser.find_element_by_id('answer')
    ans_element.send_keys(str(ans))

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()