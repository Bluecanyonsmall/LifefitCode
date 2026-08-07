from playwright.sync_api import sync_playwright

MESSAGE = """よろしく"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://gamerch.com/invitation/940697")

    # ページの読み込み待ち
    page.wait_for_load_state("networkidle")

    # コメント入力
    page.locator('textarea[name="body"]').fill(MESSAGE)

    # 「投稿する」ボタンをクリック
    page.get_by_role("button", name="投稿する").click()

    # 投稿完了まで少し待つ
    page.wait_for_timeout(5000)

    browser.close()