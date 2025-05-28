import pytest
from config.data import Data
from pages.login_page import LoginPage
#from pages.dashboard_page import DashboardPage
#from pages.personal_page import PersonalPage


class BaseTest:

    data: Data

    login_page: LoginPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
   