import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    LOGIN_FIELD = ("xpath", "//div[@class='auth__form']/descendant::input[@placeholder='Введите почту']")
    PASSWORD_FIELD = ("xpath", "//div[@class='auth__form']/descendant::input[@type='password']")
    SUBMIT_BUTTON = ("xpath", "//button[.//span[contains(text(), 'Войти')]]")
    
    @allure.step("Ввод логина")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD)).send_keys(login)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Нажатие кнопки <Войти>")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        # Ждем, пока URL изменится, то есть произойдет редирект
        self.wait.until(lambda driver: driver.current_url != self.PAGE_URL) 
       
    @allure.step("Проверка перенаправления после авторизации")
    def check_after_submit_redirect(self):       
        current_url = self.driver.current_url
        assert current_url != self.PAGE_URL, f"Предполагалось что будет перенаправление после авторизации, но получили URL {current_url}" 
        