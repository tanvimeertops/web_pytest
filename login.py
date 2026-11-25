import time
def test_login(page):
    p1=page
    p1.goto("https://www.saucedemo.com/")
    time.sleep(5)

    # page.locator("#user-name").fill("standard_user")
    # page.locator("[name='user-name']").fill("standard_user")
    # page.locator(".input_error.form_input").fill("standard_user")
    #page.locator("input[placeholder='Username']").fill("standard_user")
    #page.locator("[placeholder='Username']").fill("standard_user")
    # page.locator("[name*='user-']").fill("standard_user")
    # page.locator("[id^='login-']").click()
    # page.locator("[id$='button']").click()
    # page.locator("form input[type='text']").fill("bhbsdhbsd")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    time.sleep(1)
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    time.sleep(1)
    page.locator("[data-test=\"login-button\"]").click()

    time.sleep(5)