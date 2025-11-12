import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestConstructor:
    
    @pytest.mark.parametrize("section,locator,expected_text", [
        ("buns", Locators.buns_block, "Булки"),
        ("sauces", Locators.sauces_block, "Соусы"), 
        ("fillings", Locators.fillings_block, "Начинки")
    ])
    def test_navigate_to_sections(self, driver, wait, section, locator, expected_text):
        """Параметризованный тест перехода по разделам конструктора"""
        
        # Для теста булок добавляем дополнительный шаг - сначала переходим к соусам
        if section == "buns":
            wait.until(EC.visibility_of_element_located(Locators.sauces_block))
            driver.find_element(*Locators.sauces_block).click()
            wait.until(EC.visibility_of_element_located(Locators.buns_block))
        
        # Переход к целевому разделу
        wait.until(EC.visibility_of_element_located(locator))
        driver.find_element(*locator).click()
        
        # Проверяем, что раздел активен (используем ваш локатор current_section)
        wait.until(EC.visibility_of_element_located(Locators.current_section))
        current_section = driver.find_element(*Locators.current_section)
        assert expected_text in current_section.text, \
            f"Ожидался раздел '{expected_text}', но получен: {current_section.text}"