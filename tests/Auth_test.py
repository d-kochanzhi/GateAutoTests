import time
import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Страница авторизации")
class TestAuthFeature(BaseTest):

    @allure.title("Проверка входа")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_login_logout(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.make_screenshot("Auth_Result")
        self.login_page.check_after_submit_redirect()
  
        
     

