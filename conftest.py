import pytest
from playwright.sync_api import sync_playwright
import time
@pytest.fixture(params=["firefox","webkit","msedge","chromium"])
def page(request):
    print("Setting up the browser for testing...")

    with sync_playwright() as p:
        if request.param=="msedge":
         browser=p.chromium.launch(channel="msedge",headless=False)
       else:
         browser_type=getattr(p,request.param)
         browser=browser_type.launch(headless=False)
        page=browser.new_page()
        yield page  


        print("\n--- Closing Browser ---")
        browser.close()
