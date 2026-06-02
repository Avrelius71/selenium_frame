import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Функция для расчета (из задания)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Инициализация браузера
browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("https://suninjuly.github.io/get_attribute.html")
    xc = browser.find_element("xpath", "//h2/img[@id='treasure']")
    x = xc.get_attribute('valuex')
    y = calc(x)
    print(f"Рассчитанное значение y: {y}")

    # 4. Вводим ответ в текстовое поле (у него id="answer")
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot" (id="robotCheckbox")
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!" (id="robotsRule")
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    # 7. Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # 8. Ждем 10 секунд, чтобы увидеть и скопировать код из всплывающего окна (alert)
    print("Ждем 10 секунд для просмотра результата...")
    time.sleep(10)

finally:
    # Гарантированно закрываем браузер даже при ошибке
    browser.quit()