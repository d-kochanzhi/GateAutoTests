# LiveCoding

pip3 install -r requirements.txt

pytest --alluredir=allure-results

 .\run.bat

npm install -g npm@11.4.0

npm install -g allure-commandline
npm config get prefix

allure generate --clean -o allure-report allure-results

allure serve allure-results
