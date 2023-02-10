from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument(f"--user-data-dir=C:/Users/<username>/AppData/Local/Google/Chrome/User Data/profiledata")# nは数字
options.add_argument(f"--profile-directory=Profile 2")#アカウントごとにnが変わる
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def update_status(tweet_content):
    """
    update_status(tweet_content | Str)
    """
    driver.get("https://twitter.com/compose/tweet")
    driver.implicitly_wait(5)
    driver.find_element(by=By.CLASS_NAME, value="notranslate").send_keys(tweet_content)
    driver.find_element(by=By.XPATH, value="//div[@data-testid='tweetButton']").click()
