from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

GAME_URL = "https://rugugu.jp/2048/"

driver = webdriver.Chrome()

try:
    driver.get(GAME_URL)
    time.sleep(2)

    game_board = driver.find_element(By.TAG_NAME, 'body')

    while True:
        for action in [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]:
            game_board.send_keys(action)
            time.sleep(0.1)

except Exception as e:
    print(f"エラーが発生しました: {e}")




