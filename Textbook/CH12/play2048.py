from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

GAME_URL = "https://play2048.co/"

driver = webdriver.Chrome()

try:
    driver.get(GAME_URL)
    time.sleep(2)
    
    game_board = driver.find_element_by_tag_name('body')

    while True:
        for action in [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]:
            game_board.send_keys(action)
            time.sleep(0.1)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

