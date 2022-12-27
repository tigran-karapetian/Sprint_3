from selenium.webdriver.common.by import By
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# тест переход по клику на «Конструктор»
def test_go_to_constructor(driver):
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Constructor_Button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# тест переход в конструктор по клику на логотип Stellar Burgers
def test_click_to_stellar_burgers_logo(driver):
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Stellar_Burgers_Logo).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
