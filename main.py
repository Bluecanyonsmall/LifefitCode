import random
from playwright.sync_api import sync_playwright

NAME_LIST = ["渚", "あかり", "さくら", "ひなた", "みなみ", "ゆい", "りん", "はるか", "あおい", "まなみ"]

MESSAGE = """🛒【50 WAON POINT】イオンのお買い物がお得に！✨

iAEONアプリ新規登録で 50 WAON POINT が貰えます🎁


📲アプリDL : 

https://iaeon.go.link/6EIuW

🔑紹介コード : A06-3Q7H6WLCVPC


💡獲得の手順

①アプリDL後、新規登録画面で【コード入力】

②画面に従い会員登録＆カード登録（WAON/イオンカード等）で完了！


ぜひご活用ください😊"""

MY_CODE = "A06-3Q7H6WLCVPC"

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