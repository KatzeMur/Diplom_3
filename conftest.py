import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = os.path.abspath("chromedriver/chromedriver-win64/chromedriver.exe")
chrome_service = Service(executable_path=driver_path)

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome(service=chrome_service)
    else:
        driver = webdriver.Firefox()
    
    yield driver
    driver.quit()
    