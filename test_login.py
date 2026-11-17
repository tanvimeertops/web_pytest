import pytest
from playwright.sync_api import sync_playwright
import time


def test_login(page):
    page = page
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    time.sleep(2)
    page.click("[data-test=\"login-button\"]")
    time.sleep(5)

    assert page.url=="https://www.saucedemo.com/inventory.html","Login Failed"

    print("\n--- Test Completed ---")