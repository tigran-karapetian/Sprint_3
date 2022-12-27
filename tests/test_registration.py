from selenium.webdriver.common.by import By
from locators import TestLocators


# Проверка успешной регистрации
def test_correct_registration(driver, email_generator):
    driver.find_element(*TestLocators.personal_area).click()
    driver.find_element(*TestLocators.registration_button_main_page).click()
    driver.find_element(*TestLocators.name).send_keys("Тигран")
    driver.find_element(*TestLocators.email).send_keys(email_generator)
    driver.find_element(*TestLocators.password).send_keys("12345678")
    driver.find_element(*TestLocators.registration_register_button).click()

    element = driver.find_element(By.XPATH, "//html/body/div[1]/div/main/div/form/button")
    assert driver.find_element(By.XPATH, "//html/body/div[1]/div/main/div/form/button") == element


# Проверка ошибки для некорректного пароля
def test_erorr_text_for_incorrect_password(driver, email_generator):
    driver.find_element(*TestLocators.personal_area).click()
    driver.find_element(*TestLocators.registration_button_main_page).click()
    driver.find_element(*TestLocators.name).send_keys("Тигран")
    driver.find_element(*TestLocators.email).send_keys(email_generator)
    driver.find_element(*TestLocators.password).send_keys("1234")
    driver.find_element(*TestLocators.registration_register_button).click()

    error = driver.find_element(By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[3]/div/p").text
    assert error == 'Некорректный пароль'
