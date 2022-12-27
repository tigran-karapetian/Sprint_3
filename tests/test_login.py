from selenium.webdriver.common.by import By
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# тест вход по кнопке «Войти в аккаунт» на главной странице
def test_login_on_the_main_page(driver):
    driver.find_element(*TestLocators.Enter_Button_Main_Page).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.Checkout_Button)
    assert element == driver.find_element(*TestLocators.Checkout_Button)


# тест вход через Личный кабинет
def test_login_through_the_button_personal_account(driver):
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.Checkout_Button)
    assert element == driver.find_element(*TestLocators.Checkout_Button)


# тест вход через кнопку в форме регистрации
def test_login_through_registration_button(driver, email_generator):
    driver.find_element(*TestLocators.Personal_Area).click()
    driver.find_element(*TestLocators.Registration_Button_Main_Page).click()
    driver.find_element(*TestLocators.Name).send_keys("Тигран")
    email = email_generator
    driver.find_element(*TestLocators.Email).send_keys(email)
    driver.find_element(*TestLocators.Password).send_keys("12345678")
    driver.find_element(*TestLocators.Registration_Register_Button).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
    driver.find_element(*TestLocators.Email_Login_Page).send_keys(email)
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.Checkout_Button)
    assert element == driver.find_element(*TestLocators.Checkout_Button)


# тест вход через кнопку в форме восстановления пароля
def test_login_through_password_recovery(driver):
    driver.find_element(*TestLocators.Enter_Button_Main_Page).click()
    driver.find_element(*TestLocators.Recovery_Password_Button).click()
    driver.find_element(*TestLocators.Enter_Button_Recovery_Page).click()
    driver.find_element(*TestLocators.Email_Login_Page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.Password_Login_Page).send_keys("12345678")
    driver.find_element(*TestLocators.Enter_Button_Login_Page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.Checkout_Button)
    assert element == driver.find_element(*TestLocators.Checkout_Button)
