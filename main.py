from playwright.sync_api import sync_playwright

MESSAGE = """はじめやすく、つづくフィットネスジム💪✨

一緒に #ライフフィット で運動はじめませんか？🔰


🎁今なら「招待クーポンコード」で定期チケットが初回1000円OFFに🎫🉐✨✨


招待クーポンコード👉FR3U94TR9U


入会はこちらから👉

https://lifefit.go.link/856lx"""

MY_CODE = "FR3U94TR9U"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://gamerch.com/invitation/940697",
        wait_until="domcontentloaded",
        timeout=60000
    )

    # 最新コメント本文取得
    latest_comment = page.locator(
        'xpath=//*[@id="commentApp"]/div/div[2]/ul/li[1]/div[2]/div[2]'
    ).inner_text()

    print("最新コメント:")
    print(latest_comment)

    # 自分の投稿か確認
    if MY_CODE in latest_comment:
        print("自分の投稿を確認 → 投稿しません")

    else:
        print("他人の投稿 → コメントします")

        # コメント入力欄を開く
        page.locator("button.insert-post-area").first.click()

        textarea = page.locator('textarea[name="body"]')
        textarea.wait_for(timeout=30000)

        textarea.fill(MESSAGE)

        # 投稿
        page.get_by_role("button", name="投稿する").click()

        print("投稿完了")

        page.wait_for_timeout(5000)

    browser.close()