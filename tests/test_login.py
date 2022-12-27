from selenium.webdriver.common.by import By
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# тест вход по кнопке «Войти в аккаунт» на главной странице
def test_login_on_the_main_page(driver):
    driver.find_element(*TestLocators.enter_button_main_page).click()
    driver.find_element(*TestLocators.email_login_page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.password_login_page).send_keys("12345678")
    driver.find_element(*TestLocators.enter_button_login_page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.checkout_button)
    assert element == driver.find_element(*TestLocators.checkout_button)


# тест вход через Личный кабинет
def test_login_through_the_button_personal_account(driver):
    driver.find_element(*TestLocators.personal_area).click()
    driver.find_element(*TestLocators.email_login_page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.password_login_page).send_keys("12345678")
    driver.find_element(*TestLocators.enter_button_login_page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.checkout_button)
    assert element == driver.find_element(*TestLocators.checkout_button)


# тест вход через кнопку в форме регистрации
def test_login_through_registration_button(driver, email_generator):
    driver.find_element(*TestLocators.personal_area).click()
    driver.find_element(*TestLocators.registration_button_main_page).click()
    driver.find_element(*TestLocators.name).send_keys("Тигран")
    email = email_generator
    driver.find_element(*TestLocators.email).send_keys(email)
    driver.find_element(*TestLocators.password).send_keys("12345678")
    driver.find_element(*TestLocators.registration_register_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
    driver.find_element(*TestLocators.email_login_page).send_keys(email)
    driver.find_element(*TestLocators.password_login_page).send_keys("12345678")
    driver.find_element(*TestLocators.enter_button_login_page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.checkout_button)
    assert element == driver.find_element(*TestLocators.checkout_button)


# тест вход через кнопку в форме восстановления пароля
def test_login_through_password_recovery(driver):
    driver.find_element(*TestLocators.enter_button_main_page).click()
    driver.find_element(*TestLocators.recovery_password_button).click()
    driver.find_element(*TestLocators.enter_button_recovery_page).click()
    driver.find_element(*TestLocators.email_login_page).send_keys("karapetiantm@gmail.com")
    driver.find_element(*TestLocators.password_login_page).send_keys("12345678")
    driver.find_element(*TestLocators.enter_button_login_page).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(*TestLocators.checkout_button)
    assert element == driver.find_element(*TestLocators.checkout_button)
