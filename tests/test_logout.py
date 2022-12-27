from selenium.webdriver.common.by import By
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


#тест выход по кнопке «Выйти» в личном кабинете
def test_logout_button_in_personal_account(driver):
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.Logout_Button_Personal_Account_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

