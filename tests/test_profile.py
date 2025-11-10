from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestProfile:
    
    def login(self, driver, wait):
        """Вспомогательный метод для авторизации"""
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        driver.find_element(*Locators.fields_email_auth).send_keys("test179@yandex.ru")
        driver.find_element(*Locators.fields_password_auth).send_keys("password123")
        driver.find_element(*Locators.button_login).click()
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))

    def test_navigate_to_personal_account(self, driver, wait):
        """Переход в личный кабинет"""
        self.login(driver, wait)
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.profile))
        assert driver.find_element(*Locators.profile).is_displayed()

    def test_navigate_from_profile_to_constructor_via_button(self, driver, wait):
        """Переход из личного кабинета в конструктор по кнопке"""
        self.login(driver, wait)
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.header_of_page_constructor).click()
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    def test_navigate_from_profile_to_constructor_via_logo(self, driver, wait):
        """Переход из личного кабинета в конструктор по логотипу"""
        self.login(driver, wait)
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logo_Stellar_Burgers).click()
        wait.until(EC.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    def test_logout(self, driver, wait):
        """Выход из аккаунта"""
        self.login(driver, wait)
        driver.find_element(*Locators.button_personal_account).click()
        wait.until(EC.visibility_of_element_located(Locators.button_logout))
        driver.find_element(*Locators.button_logout).click()
        wait.until(EC.visibility_of_element_located(Locators.login_title))
        assert driver.find_element(*Locators.login_title).is_displayed()