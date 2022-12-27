from selenium.webdriver.common.by import By


class TestLocators:
    # Кнопка Личный кабинет
    personal_area = By.XPATH, "//html/body/div[1]/div/header/nav/a"
    # Кнопка Зарегистрироваться на главной странице
    registration_button_main_page = By.CLASS_NAME, "Auth_link__1fOlj"
    # Поле Имя на форме регистрации
    name = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input"
    # Поле Email на форме регистрации
    email = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"
    # Поле Пароль на форме регистрации
    password = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[3]/div/div/input"
    # Кнопка Зарегистрироваться на форме регистрации
    registration_register_button = By.XPATH, "//html/body/div[1]/div/main/div/form/button"
    # Кнопка Войти в аккаунт на главной странице
    enter_button_main_page = By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button"
    #Поле Email на странице входа
    email_login_page = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input"
    #Поле Пароль на странице входа
    password_login_page = By.XPATH, "//html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"
    #Кнопка Войти на странице входа
    enter_button_login_page = By.XPATH, "/html/body/div[1]/div/main/div/form/button"
    #Кнопка оформить заказ
    checkout_button = By.XPATH, ".//button[text()='Оформить заказ']"
    #Кнопка восстановить пароль
    recovery_password_button = By.XPATH, "/html/body/div[1]/div/main/div/div/p[2]/a"
    #Email на  форме восстановления пароля
    email_for_password_recovery = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset/div/div/input"
    #Кнопка восстановить
    recovery_button = "/html/body/div[1]/div/main/div/form/button"
    #Кнопка Войти на форме восттановления пароля
    enter_button_recovery_page = By.XPATH, "/html/body/div[1]/div/main/div/div/p/a"
    #Кнопка Конструктор в личном кабинете
    constructor_button = By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[1]/a"
    #Логотип Stellar Burgers в личном кабинете
    stellar_burgers_logo = By.XPATH, "/html/body/div[1]/div/header/nav/div/a"
    #Кнопка выход в личном кабинете
    logout_button_personal_account_Page = By.XPATH, "/html/body/div[1]/div/main/div/nav/ul/li[3]/button"
    #Кнопка Булки
    buns_button = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[1]"
    #Кнопка Соусы
    sauces_button = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[2]"
    #Кнопка Начинки
    toppings_button = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[3]"


