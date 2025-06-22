import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv

load_dotenv()

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    if HEADLESS:
        # New, native Headless mode
        options.add_argument("--headless=new")
        # Often used in Lambda, Cloud Functions scenarios and Docker
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()