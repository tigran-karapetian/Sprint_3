import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import secrets


# Инициализация драйвера
@pytest.fixture
def driver():
    service = Service(executable_path='/Users/tigrankarapetian/PycharmProjects/Sprint_3/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


# Генерация рандомных логинов
@pytest.fixture
def email_generator():
    return f"{secrets.token_hex(5)}@gmail.com"
