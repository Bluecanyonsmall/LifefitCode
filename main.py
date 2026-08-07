from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(
        "https://gamerch.com/invitation/940697",
        wait_until="domcontentloaded",
        timeout=60000
    )

    html = page.content()

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML保存完了")

    browser.close()