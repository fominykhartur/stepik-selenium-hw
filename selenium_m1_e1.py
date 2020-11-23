from selenium import webdriver
import time

path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    reguired_input1 = browser.find_element_by_css_selector("input.first[required]")
    reguired_input1.send_keys('1')
    reguired_input2 = browser.find_element_by_css_selector("input.second[required]")
    reguired_input2.send_keys('1')
    reguired_input3 = browser.find_element_by_css_selector("input.third[required]")
    reguired_input3.send_keys('1')
    
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()