import pytest
from .pages.main_page import MainPage

link = 'https://www.saucedemo.com/'


#class TestMainPage:

@pytest.mark.smoke
def test_login(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.login()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', '!!!You did not entered!!!'

