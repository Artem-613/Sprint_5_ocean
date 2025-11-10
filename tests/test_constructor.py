from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestConstructor:
    
    def test_navigate_to_buns_section(self, driver, wait):
        """Переход к разделу 'Булки'"""
        # Сначала переходим к другому разделу
        wait.until(EC.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        
        # Затем возвращаемся к булкам
        wait.until(EC.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.buns_block).click()
        
        # Проверяем, что раздел активен
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        assert "Булки" in current_section.text

    def test_navigate_to_sauces_section(self, driver, wait):
        """Переход к разделу 'Соусы'"""
        wait.until(EC.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        
        # Проверяем, что раздел активен
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        assert "Соусы" in current_section.text

    def test_navigate_to_fillings_section(self, driver, wait):
        """Переход к разделу 'Начинки'"""
        wait.until(EC.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        
        # Проверяем, что раздел активен
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        assert "Начинки" in current_section.text