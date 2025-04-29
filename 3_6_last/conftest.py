import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Функция для добавления кастомной опции в pytest
def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose browser language (e.g., es, fr)")


# Фикстура для создания и настройки браузера
@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение языка из командной строки
    user_language = request.config.getoption("language")

    # Настройки Chrome
    options = Options()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': user_language}
    )

    # Создаём экземпляр браузера с настройками
    browser = webdriver.Chrome(options=options)

    # Передаём браузер в тест
    yield browser

    # Закрываем браузер после завершения теста
    browser.quit()