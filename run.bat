@echo off
set HOST=http://www.msp.lan
pytest --alluredir=allure-results
allure generate --clean -o allure-report allure-results
allure serve allure-results