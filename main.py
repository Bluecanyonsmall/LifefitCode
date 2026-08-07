from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://gamerch.com/invitation/940697",
        wait_until="domcontentloaded",
        timeout=60000
    )

    print(page.title())

    browser.close()