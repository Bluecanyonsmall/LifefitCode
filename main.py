from playwright.sync_api import sync_playwright

NAME_LIST = ["筋トレ！", "フィットネス！", "運動大好き！", "健康第一！", 
             "ライフフィット！", "体力向上！", "ダイエット！", "ストレス解消！", 
             "元気いっぱい！", "体を動かそう！", "健康生活！", "運動習慣！", 
             "フィットネス仲間！", "体力アップ！", "健康維持！", "運動チャレンジ！", 
             "ライフスタイル改善！", "体を鍛えよう！", "健康美！", "運動で元気に！", "鋼の意志",
             "限界一歩前", "筋肉貯金", "鉄塊", "今日も追い込み", "三日坊主卒業生", "可動域警察", 
             "重量に恋してる", "筋肉育成中", "明日の自分に勝つ"]

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
    try:
        latest_comment = page.locator(
            'xpath=//*[@id="commentApp"]/div/div[2]/ul/li[2]/div[2]/div[2]'
        ).inner_text()

    except Exception as e:
        latest_comment = "コメントの取得でエラー発生"

    print("最新コメント:")
    print(latest_comment)

    # 自分の投稿か確認
    if MY_CODE in latest_comment:
        print("自分の投稿を確認 → 投稿しません")

    else:
        print("他人の投稿 → コメントします")

        # コメント入力欄を開く
        page.locator("button.insert-post-area").first.click()

        inputarea = page.locator('input[name="nickname"]')
        textarea = page.locator('textarea[name="body"]')
        textarea.wait_for(timeout=10000)

        inputarea.fill(NAME_LIST[random.randint(0, len(NAME_LIST) - 1)])
        textarea.fill(MESSAGE)

        # 投稿
        page.get_by_role("button", name="投稿する").click()

        print("投稿完了")

        page.wait_for_timeout(1000)

    browser.close()