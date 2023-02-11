from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#-----------------------------------------------------------------------------------------------------------------------
# Latest Update 2023/02/11
# Add create_block,get_followers,create_mute

# Latest Update 2023/02/11 13:04
# Add destroy_block,destroy_mute,is_follower

# Latest Update 2023/02/11 14:25
# Add destroy_status

#-----------------------------------------------------------------------------------------------------------------------


options = Options()
options.add_argument("--user-data-dir=C:/Users/<username>/AppData/Local/Google/Chrome/User Data/profiledata")
options.add_argument("--profile-directory=Profile 2")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# Post, retrieve, and engage with Tweets--------------------------------------------------------------------------------
def update_status(tweet_content):
    """
    update_status(tweet_content | Str)
    """
    driver.get("https://twitter.com/compose/tweet")
    driver.implicitly_wait(1)
    driver.find_element(by=By.CLASS_NAME, value="notranslate").send_keys(tweet_content)
    driver.find_element(by=By.XPATH, value="//div[@data-testid='tweetButton']").click()

def destroy_status(tweet_url):
    driver.get(tweet_url)
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, value='//div[@data-testid="caret"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.CLASS_NAME,
                        value='css-1dbjc4n.r-1loqt21.r-18u37iz.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg.r-13qz1uu').click()
    driver.find_element(By.XPATH, value='//div[@data-testid="confirmationSheetConfirm"]').click()


# Follow, search, and get users-----------------------------------------------------------------------------------------
def get_followers(screen_name): # cannot run
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
    driver.implicitly_wait(1)
    driver.find_element(By.CLASS_NAME,value='css-18t94o4.css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1phboty.r-rs99b7.r-6gpygo.r-1kb76zh.r-2yi16.r-1qi8awa.r-1ny4l3l.r-o7ynqc.r-6416eg.r-lrvibr').click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.XPATH, value='//div[@data-testid="block"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.XPATH, '//div[@data-testid="confirmationSheetConfirm"]').click()

def destroy_block(screen_name):
    """
    destroy_block(screen_name | Str)
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_blocknow = driver.find_element(By.XPATH, value='//div[@data-testid="empty_state_body_text"]')
        if is_blocknow:
            driver.implicitly_wait(0.5)
            driver.find_element(By.CLASS_NAME,
                                value="css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr").click()
            driver.implicitly_wait(0.5)
            driver.find_element(By.CLASS_NAME,
                                value="css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-6gpygo.r-peo1c.r-1ps3wis.r-1ny4l3l.r-1udh08x.r-1guathk.r-1udbk01.r-o7ynqc.r-6416eg.r-lrvibr.r-3s2u2q").click()
    except selenium.common.exceptions.NoSuchElementException:
        print("このユーザーをブロックしていませんでした")


def create_mute(screen_name):
    """
    create_mute(screen_name | Str)
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    driver.find_element(By.CLASS_NAME,value="css-18t94o4.css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1phboty.r-rs99b7.r-6gpygo.r-1kb76zh.r-2yi16.r-1qi8awa.r-1ny4l3l.r-o7ynqc.r-6416eg.r-lrvibr").click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.XPATH, value='//div[@data-testid="mute"]').click()

def destroy_mute(screen_name):
    """
    destroy_mute(screen_name | Str)
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        driver.find_element(By.XPATH, value='//span[@data-testid="unmuteLink"]')
        driver.find_element(By.XPATH, value='//div[@data-testid="userActions"]').click()
        driver.find_element(By.XPATH, value='//div[@data-testid="mute"]').click()
    except selenium.common.exceptions.NoSuchElementException:
        print("ミュートしていませんでした")

def is_follower(screen_name):
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_follower = driver.find_element(By.XPATH, value='//div[@data-testid="userFollowIndicator"]')
        if is_follower:
            return True
    except selenium.common.exceptions.NoSuchElementException:
        return False
