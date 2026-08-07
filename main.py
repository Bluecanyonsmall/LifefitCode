from playwright.sync_api import sync_playwright

MESSAGE = "FR3U94TR9U"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://gamerch.com/invitation/940697")

    page.wait_for_load_state("networkidle")

    page.locator('textarea[name="body"]').fill(MESSAGE)

    page.get_by_role("button", name="投稿する").click()

    page.wait_for_timeout(5000)

    browser.close()