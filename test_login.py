import pytest
from playwright.sync_api import sync_playwright
import time
@pytest.fixture
def setup_browser():
    print("Setting up the browser for testing...")

    with sync_playwright() as p:
        browser =p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.saucedemo.com/")
        yield page  


        print("\n--- Closing Browser ---")
        browser.close()


def test_login(setup_browser):
    page = setup_browser
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    time.sleep(2)
    page.click("[data-test=\"login-button\"]")
    time.sleep(5)

    assert page.url=="https://www.saucedemo.com/inventory.html","Login Failed"

    print("\n--- Test Completed ---")