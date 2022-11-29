import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/'

@pytest.fixture(scope='class')
def browser():
    print('\nStart browser...')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print('\nClose browser...')
    browser.quit()


class TestMainPage:

    def test_1(self, browser):
        browser.get(link)

    def test_2(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
