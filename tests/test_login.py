from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestLogin:
    
    def test_login_via_main_page_button(self, driver, wait):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        
        # Заполнение формы авторизации
        driver.find_element(*Locators.fields_email_auth).send_keys("test179@yandex.ru")
        driver.find_element(*Locators.fields_password_auth).send_keys("password123")
        driver.find_element(*Locators.button_login).click()
        
        # Проверка успешного входа
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    def test_login_via_personal_account_button(self, driver, wait):
        """Вход через кнопку «Личный кабинет»"""
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        
        # Заполнение формы авторизации
        driver.find_element(*Locators.fields_email_auth).send_keys("test179@yandex.ru")
        driver.find_element(*Locators.fields_password_auth).send_keys("password123")
        driver.find_element(*Locators.button_login).click()
        
        # Проверка успешного входа
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    def test_login_via_registration_form(self, driver, wait):
        """Вход через кнопку в форме регистрации"""
        driver.find_element(*Locators.button_login_in_main).click()
        wait.until(EC.visibility_of_element_located(Locators.register_button_login))
        driver.find_element(*Locators.register_button_login).click()
        wait.until(EC.visibility_of_element_located(Locators.button_login_in_registration_form))
        driver.find_element(*Locators.button_login_in_registration_form).click()
        
        # Заполнение формы авторизации
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys("test179@yandex.ru")
        driver.find_element(*Locators.fields_password_auth).send_keys("password123")
        driver.find_element(*Locators.button_login).click()
        
        # Проверка успешного входа
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    def test_login_via_password_recovery_form(self, driver, wait):
        """Вход через кнопку в форме восстановления пароля"""
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.button_forgot_password))
        driver.find_element(*Locators.button_forgot_password).click()
        wait.until(EC.visibility_of_element_located(Locators.button_login_passwd_recovery_form))
        driver.find_element(*Locators.button_login_passwd_recovery_form).click()
        
        # Заполнение формы авторизации
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys("test179@yandex.ru")
        driver.find_element(*Locators.fields_password_auth).send_keys("password123")
        driver.find_element(*Locators.button_login).click()
        
        # Проверка успешного входа
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()