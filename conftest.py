import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators  # добавляем импорт

# Добавляем корневую директорию в путь Python
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

@pytest.fixture(scope='function')
def driver():
    # Настройки для Chrome
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')  # исправил опечатку
    chrome_options.add_argument('--window-size=1920,1080')

    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Указываем URL напрямую
    driver.get('https://stellarburgers.education-services.ru/')

    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def wait(driver):
    return WebDriverWait(driver, 10)

# ДОБАВЛЯЕМ НОВУЮ ФИКСТУРУ ДЛЯ ЛОГИНА
@pytest.fixture(scope='function')
def login_user(driver, wait):
    """Фикстура для авторизации пользователя"""
    def _login(email="test179@yandex.ru", password="password123"):
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys(email)
        driver.find_element(*Locators.fields_password_auth).send_keys(password)
        driver.find_element(*Locators.button_login).click()
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
    
    return _login