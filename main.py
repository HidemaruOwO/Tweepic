from flask import Flask, request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

@app.route('/')
def get_twitter_icon():
    # ユーザーIDを取得する
    user_id = request.args.get('id')

    # ヘッドレスChromeを起動する
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    # Twitterのプロフィールページにアクセスする
    driver.get(f'https://twitter.com/{user_id}/photo')

    # 要素が表示されるまで待つ
    wait = WebDriverWait(driver, 10)
    icon = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "img.css-9pa8cd")))

    # JavaScriptを実行してアイコンのURLを取得する
    icon_url = driver.execute_script("return arguments[0].src;", icon)

    # ブラウザを終了する
    driver.quit()

    # 結果を文字列形式で返す
    return str(icon_url)

if __name__ == '__main__':
    app.run()

