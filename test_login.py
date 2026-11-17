import pytest
from playwright.sync_api import sync_playwright

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
    page.fill("#username", "testuser")
    page.fill("#password", "password123")
    page.click("#login-button")

    # Add assertions to verify successful login
    assert page.url == "https://example.com/dashboard"