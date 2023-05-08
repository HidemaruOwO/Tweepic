from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_twitter_icon():
    # idをクエリから取得する
    user_id = request.args.get('id')

    # ヘッドレスモードを有効にする
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

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

    # icon_urlを文字列で返す
    return icon_url


if __name__ == '__main__':
    app.run()

