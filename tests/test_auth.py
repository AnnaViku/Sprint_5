import unittest
from selenium import webdriver
from locators import *

class TestStellarBurgers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def tearDown(self):
        self.driver.quit()

    def test_successful_registration(self):
        self.driver.find_element(*REGISTER_NAME_INPUT).send_keys("Имя")
        self.driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("test@example.com")
        self.driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123456")
        self.driver.find_element(*REGISTER_BUTTON).click()
        # Здесь добавьте проверку, что регистрация прошла успешно

    def test_incorrect_password_registration(self):
        self.driver.find_element(*REGISTER_NAME_INPUT).send_keys("Имя")
        self.driver.find_element(*REGISTER_EMAIL_INPUT).send_keys("test@example.com")
        self.driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")
        self.driver.find_element(*REGISTER_BUTTON).click()
        # Здесь добавьте проверку, что ошибка отображается

    def test_login_buttons_functionality(self):
        # 测试 кнопка "Войти в аккаунт"
        self.driver.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
        # Здесь добавьте проверки, что переход произошел

    def test_logout_functionality(self):
        # Залогиньте пользователя для теста
        self.test_successful_registration()  # Или другие действия для логина
        self.driver.find_element(*PERSONAL_CABINET_LOGOUT_BUTTON).click()
        # Здесь добавьте проверку, что пользователь вышел

    def test_constructor_tabs(self):
        self.driver.find_element(*CONSTRUCTOR_LINK).click()
        self.driver.find_element(*BUNS_TAB).click()
        # Здесь добавьте проверки на элементы внутри вкладки булок
        self.driver.find_element(*SAUCES_TAB).click()
        # Здесь добавьте проверки на элементы внутри вкладки соусов
        self.driver.find_element(*FILLINGS_TAB).click()
        # Здесь добавьте проверки на элементы внутри вкладки начинок

if __name__ == "__main__":
    unittest.main()