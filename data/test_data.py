import random
import string


class TestData:
    """Тестовые данные для автотестов"""
    
    # URL
    BASE_URL = "https://stellarburgers.education-services.ru/"
    
    # Существующий пользователь (замени на свои данные)
    EXISTING_USER_EMAIL = "test179@yandex.ru"
    EXISTING_USER_PASSWORD = "password123"
    EXISTING_USER_NAME = "Тестовый Пользователь"


class DataGenerator:
    """Генераторы тестовых данных"""
    
    @staticmethod
    def generate_email():
        """Генератор уникального email"""
        names = ["ivanov", "petrov", "sidorov", "smirnov", "kuznetsov"]
        name = random.choice(names)
        numbers = ''.join(random.choices(string.digits, k=3))
        return f"{name}{numbers}@yandex.ru"
    
    @staticmethod
    def generate_password(length=6):
        """Генератор пароля"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    
    @staticmethod
    def generate_name():
        """Генератор имени"""
        names = ["Иван", "Петр", "Мария", "Анна", "Сергей"]
        surnames = ["Иванов", "Петров", "Сидорова", "Смирнова"]
        return f"{random.choice(names)} {random.choice(surnames)}"
    
class Urls:
    STELLAR_BURGERS_URL = "https://stellarburgers.education-services.ru/"