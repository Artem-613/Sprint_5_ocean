import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data.test_data import DataGenerator

class TestRegistration:
    
    def test_successful_registration(self, driver, wait):
        """Успешная регистрация с валидными данными"""
        # Переход к форме регистрации
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        
        # Заполнение формы
        wait.until(EC.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(DataGenerator.generate_name())
        driver.find_element(*Locators.fields_email).send_keys(DataGenerator.generate_email())
        driver.find_element(*Locators.fields_password).send_keys(DataGenerator.generate_password(8))
        driver.find_element(*Locators.button_submit).click()
        
        # Проверка успешной регистрации
        is_login_page_visible = EC.visibility_of_element_located(Locators.login_title)(driver)
        is_main_page_visible = EC.visibility_of_element_located(Locators.button_make_the_order)(driver)
        
        assert is_login_page_visible or is_main_page_visible, \
            "После регистрации не отобразилась ни страница входа, ни главная страница"

    @pytest.mark.parametrize("invalid_password", ["12345", "123"])
    def test_registration_with_short_password(self, driver, wait, invalid_password):
        """Ошибка при регистрации с коротким паролем"""
        # Переход к форме регистрации
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        
        # Заполнение формы с некорректным паролем
        wait.until(EC.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(DataGenerator.generate_name())
        driver.find_element(*Locators.fields_email).send_keys(DataGenerator.generate_email())
        driver.find_element(*Locators.fields_password).send_keys(invalid_password)
        driver.find_element(*Locators.button_submit).click()
        
        # Проверка отображения ошибки для короткого пароля
        wait.until(EC.visibility_of_element_located(Locators.incorrect_password))
        assert driver.find_element(*Locators.incorrect_password).is_displayed()

    def test_registration_with_empty_password(self, driver, wait):
        """Ошибка при регистрации с пустым паролем"""
        # Переход к форме регистрации
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        
        # Заполнение формы с пустым паролем
        wait.until(EC.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(DataGenerator.generate_name())
        driver.find_element(*Locators.fields_email).send_keys(DataGenerator.generate_email())
        driver.find_element(*Locators.fields_password).send_keys(" ")
        driver.find_element(*Locators.button_submit).click()
        
        # Проверка что кнопка осталась активна (форма не отправилась)
        assert driver.find_element(*Locators.button_submit).is_enabled()