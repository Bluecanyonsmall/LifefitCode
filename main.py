from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://gamerch.com/invitation/940697")
    time(10)

    textarea = page.locator('textarea[name="body"]')
    print("textareaの数:", textarea.count())

    browser.close()