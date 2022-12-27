from selenium.webdriver.common.by import By
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# тест переходы к разделам: «Булки», «Соусы», «Начинки»
def test_click_to_toppings(driver):
    driver.find_element(*TestLocators.toppings_button).click()
    assert driver.find_element(By.XPATH,
                        ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

def test_click_to_sauces(driver):
    driver.find_element(*TestLocators.sauces_button).click()
    assert driver.find_element(By.XPATH,
                               ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

def test_click_to_buns(driver):
    driver.find_element(*TestLocators.sauces_button).click()
    driver.find_element(*TestLocators.buns_button).click()
    assert driver.find_element(By.XPATH,
                               ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
