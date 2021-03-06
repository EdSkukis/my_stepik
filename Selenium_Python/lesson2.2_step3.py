from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


#patc_chromedrie = executable_path="c:/chromedrive/chromedriver.exe"
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    y = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла