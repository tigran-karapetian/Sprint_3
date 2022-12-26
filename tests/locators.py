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
    # Кнопка Войти в аккаунт на главной странице
    Enter_Button_Main_Page = By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button"
    #Поле Email на странице входа
    Email_Login_Page = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input"
    #Поле Пароль на странице входа
    Password_Login_Page = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"
    #Кнопка Войти на странице входа
    Enter_Button_Login_Page = By.XPATH, "/html/body/div[1]/div/main/div/form/button"
    #Кнопка оформить заказ
    Checkout_Button = By.XPATH, ".//button[text()='Оформить заказ']"
    #Кнопка восстановить пароль
    Recovery_Password_Button = By.XPATH, "/html/body/div[1]/div/main/div/div/p[2]/a"
    #Email на  форме восстановления пароля
    Email_For_Password_Recovery = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset/div/div/input"
    #Кнопка восстановить
    Recovery_Button = "/html/body/div[1]/div/main/div/form/button"
    #Кнопка Войти на форме восттановления пароля
    Enter_Button_Recovery_Page = By.XPATH, "/html/body/div[1]/div/main/div/div/p/a"
    #Кнопка Конструктор в личном кабинете
    Constructor_Button = By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[1]/a"
    #Логотип Stellar Burgers в личном кабинете
    Stellar_Burgers_Logo = By.XPATH, "/html/body/div[1]/div/header/nav/div/a"
    #Кнопка выход в личном кабинете
    Logout_Button_Personal_Account_Page = By.XPATH, "/html/body/div[1]/div/main/div/nav/ul/li[3]/button"
    #Кнопка Булки
    Buns_Button = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[1]"
    #Кнопка Соусы
    Sauces_Button = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[2]"
    #Кнопка Начинки
    Toppings_Button = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[3]"


