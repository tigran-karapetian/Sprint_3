from selenium.webdriver.common.by import By
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# тест вход по кнопке «Войти в аккаунт» на главной
def test_login_on_the_main_page(driver):
    driver.find_element(*TestLocators.Enter_Button_Main_Page).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.Checkout_Button)
    #time.sleep(3)
    assert element == driver.find_element(*TestLocators.Checkout_Button)
