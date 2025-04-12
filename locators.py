from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
REGISTER_NAME_INPUT = (By.XPATH, '//input[@placeholder="Имя"]')  # Поле для ввода имени
REGISTER_EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Email"]')  # Поле для ввода email
REGISTER_PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Пароль"]')  # Поле для ввода пароля
REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка регистрации
REGISTER_ERROR_MESSAGE = (By.XPATH, '//*[@class="input__error"]')  # Сообщение об ошибке

# Локаторы для страницы входа
LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной
LOGIN_BUTTON_PERSONAL_CABINET = (By.XPATH, '//a[text()="Личный кабинет"]')  # Кнопка "Личный кабинет"
LOGIN_BUTTON_IN_REGISTER_FORM = (By.XPATH, '//a[contains(text(), "Войти")]')  # Кнопка "Войти" в форме регистрации
LOGIN_FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')  # Кнопка восстановления пароля

# Локаторы для личного кабинета
PERSONAL_CABINET_LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')  # Кнопка "Выйти"
CONSTRUCTOR_LINK = (By.XPATH, '//a[text()="Конструктор"]')  # Ссылка на Конструктор

# Локаторы для конструктора
BUNS_TAB = (By.XPATH, '//tab[@data-tab="bun"]')  # Вкладка "Булки"
SAUCES_TAB = (By.XPATH, '//tab[@data-tab="sauce"]')  # Вкладка "Соусы"
FILLINGS_TAB = (By.XPATH, '//tab[@data-tab="filling"]')  # Вкладка "Начинки"