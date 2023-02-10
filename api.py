from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

#-----------------------------------------------------------------------------------------------------------------------
# Latest change 2023/02/11
# Add create block,get_followers
#-----------------------------------------------------------------------------------------------------------------------


options = Options()
options.add_argument(f"--user-data-dir=C:/Users/<username>/AppData/Local/Google/Chrome/User Data/profiledata")
options.add_argument(f"--profile-directory=Profile 2")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# Post, retrieve, and engage with Tweets--------------------------------------------------------------------------------
def update_status(tweet_content):
    """
    update_status(tweet_content | Str)
    """
    driver.get("https://twitter.com/compose/tweet")
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="notranslate").send_keys(tweet_content)
    driver.find_element(by=By.XPATH, value="//div[@data-testid='tweetButton']").click()


# Follow, search, and get users-----------------------------------------------------------------------------------------
def get_followers(screen_name):
    """
    get_follower(screen_name | Str)
    """
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.get(f"https://twitter.com/{screen_name}/followers")
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        driver.implicitly_wait(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        usernames = driver.find_elements(By.CLASS_NAME,
                                         value="css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-1j3t67a.r-1w50u8q.r-o7ynqc.r-6416eg")
        print(usernames)


# Mute, block, and report users-----------------------------------------------------------------------------------------
def create_block(screen_name):
    """
    create_block(screen_name | Str)
    """
    driver.get(f"https://twitter.com/{screen_name}")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,
                        value="css-18t94o4.css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1phboty.r-rs99b7.r-6gpygo.r-1kb76zh.r-2yi16.r-1qi8awa.r-1ny4l3l.r-o7ynqc.r-6416eg.r-lrvibr").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, value="//div[@data-testid='block']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@data-testid="confirmationSheetConfirm"]').click()