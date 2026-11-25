import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chromium","firefox","webkit","msedge"])
def page(request):
    print("setting up browser")
    with sync_playwright() as p:
       
      #  browser= p.chromium.launch(headless=False)
      
      #  browser= p.webkit.launch(headless=False)
       
      #  browser= p.firefox.launch(headless=False)
      
       if request.param=="msedge":
         browser=p.chromium.launch(channel="msedge",headless=False)
       else:
         browser_type=getattr(p,request.param)
         browser=browser_type.launch(headless=False)
         print(f"browser type :{browser_type}")
       page=browser.new_page()

       yield page

    
       print("close browser")
       browser.close()

