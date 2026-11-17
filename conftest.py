import pytest
from playwright.sync_api import sync_playwright
import time
@pytest.fixture
def page():
    print("Setting up the browser for testing...")

    with sync_playwright() as p:
        browser =p.chromium.launch(headless=False)
        page=browser.new_page()
        yield page  


        print("\n--- Closing Browser ---")
        browser.close()