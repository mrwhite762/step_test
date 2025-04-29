import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button_is_clickable(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    # Явное ожидание кликабельности кнопки
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='add_to_basket_form']/button"))
    )

    # Проверка, что кнопка отображается и активна
    assert button.is_displayed() and button.is_enabled(), "Кнопка не кликабельна"