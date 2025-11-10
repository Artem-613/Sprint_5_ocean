import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# Добавляем корневую директорию в путь Python
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

@pytest.fixture(scope='function')
def driver():
    # Настройки для Chrome
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
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