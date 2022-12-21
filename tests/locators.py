from selenium.webdriver.common.by import By


class TestLocators:
    # Кнопка Личный кабинет
    Personal_Area = By.XPATH, "//html/body/div[1]/div/header/nav/a"
    # Кнопка Зарегистрироваться на главной странице
    Registration_Button_Main_Page = By.CLASS_NAME, "Auth_link__1fOlj"
    # Поле Имя на форме регистрации
    Name = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input"
    # Поле Email на форме регистрации
    Email = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"
    # Поле Пароль на форме регистрации
    Password = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[3]/div/div/input"
    # Кнопка Зарегистрироваться на форме регистрации
    Registration_Register_Button = By.XPATH, "//html/body/div[1]/div/main/div/form/button"
    # Кнопка Войти на главной странице
    Enter_Button_Main_Page = By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button"
    #Поле Email на странице входа
    Email_Login_Page = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input"
    #Поле Пароль на странице входа
    Password_Login_Page = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"
    #Кнопка Войти на странице входа
    Enter_Button_Login_Page = By.XPATH, ".//button[text()='Войти']"
    #Кнопка оформить заказ
    Checkout_Button = By.XPATH, ".//button[text()='Оформить заказ']"