from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import selenium

#-----------------------------------------------------------------------------------------------------------------------
# Update 2023/02/11
# Add create_block,get_followers,create_mute,destroy_block,destroy_mute,is_follower,destroy_status

# Update 2023/02/12
# Add is_Private,create_follow,destroy_follow

#-----------------------------------------------------------------------------------------------------------------------

def driver(user_data_dir_path, profile_directory):
    """
    driver(user_data_dir_path | Str, profile_directory | Str)
    """
    options = Options()
    options.add_argument(
        f"--user-data-dir={user_data_dir_path}")
    options.add_argument(f"--profile-directory={profile_directory}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Post, retrieve, and engage with Tweets--------------------------------------------------------------------------------
def update_status(driver, tweet_content):
    """
    update_status(driver, tweet_content | Str)
    mandatory -> driver
    """
    driver.get("https://twitter.com/compose/tweet")
    driver.implicitly_wait(1)
    driver.find_element(By.CLASS_NAME, value="notranslate").send_keys(tweet_content)
    driver.find_element(By.XPATH, value="//div[@data-testid='tweetButton']").click()


def destroy_status(driver, tweet_url):
    driver.get(tweet_url)
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, value='//div[@data-testid="caret"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.CLASS_NAME,
                        value='css-1dbjc4n.r-1loqt21.r-18u37iz.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg.r-13qz1uu').click()
    driver.find_element(By.XPATH, value='//div[@data-testid="confirmationSheetConfirm"]').click()

# Follow, search, and get users-----------------------------------------------------------------------------------------
def get_followers(driver, screen_name):  # cannot run
    """
    get_follower(driver, screen_name | Str)
    mandatory -> driver
    """
    followers_list = []
    driver.get(f"https://twitter.com/{screen_name}/followers")
    driver.implicitly_wait(1)
    follower = driver.find_elements(By.XPATH, value='//div[@dir="ltr"]')
    for list in follower:
        followers_list.append(list.text)
    return followers_list


def is_follower(driver, screen_name): #cannot run
    """
    is_follower(driver, screen_name | Str)
    mandatory -> driver
    return | True or False
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_follower = driver.find_element(By.XPATH, value='//div[@data-testid="userFollowIndicator"]')
        return True
    except selenium.common.exceptions.NoSuchElementException:
        return False

def is_Private(driver,screen_name):
    """
    is_Private(driver, screen_name | Str)
    mandatory -> driver
    return | True or False
    Private account -> True
    Public account -> False
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_private = driver.find_element(By.XPATH,value='//*[@data-testid="icon-lock"]')
        return True
    except selenium.common.exceptions.NoSuchElementException:
        return False

options = Options()
options.add_argument(f"--user-data-dir=C:/Users/yuich/AppData/Local/Google/Chrome/User Data/profiledata")
options.add_argument(f"--profile-directory=Profile 2")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def create_follow(driver, screen_name):
    """
    create_follow(driver, screen_name)
    mandatory -> driver
    return | True or False
    Follow now -> False
    not Follow now -> True
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_unfollow = driver.find_element(By.CLASS_NAME,value="css-18t94o4.css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr")
        if is_follow.get_attribute("data-testid").endswith("unfollow"):
            return False
    except selenium.common.exceptions.NoSuchElementException:
        driver.find_element(By.CLASS_NAME,value="css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr").click()
        return True

def destroy_follow(driver, screen_name):
    """
    destroy_follow(driver, screen_name)
    mandatory -> driver
    return | True or False
    Follow now -> True
    not Follow now -> False
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_unfollow = driver.find_element(By.CLASS_NAME,value="css-18t94o4.css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr")
        if is_follow.get_attribute("data-testid").endswith("unfollow"):
            driver.find_element(By.CLASS_NAME,
                                value="css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr").click()
            return True
    except selenium.common.exceptions.NoSuchElementException:
        return False

# Mute, block, and report users-----------------------------------------------------------------------------------------
def create_block(driver, screen_name):
    """
    create_block(driver, screen_name | Str)
    mandatory -> driver
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    is_blocked = driver.find_element(By.CLASS_NAME,value='css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr')
    if not is_blocked.get_attribute("data-testid").endswith("unblock"):
        driver.find_element(By.CLASS_NAME,  # view menu
                            value="css-18t94o4.css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1phboty.r-rs99b7.r-6gpygo.r-1kb76zh.r-2yi16.r-1qi8awa.r-1ny4l3l.r-o7ynqc.r-6416eg.r-lrvibr").click()
        driver.implicitly_wait(0.5)
        driver.find_element(By.XPATH, value="//div[@data-testid='block']").click()
        driver.implicitly_wait(0.5)
        driver.find_element(By.XPATH, '//div[@data-testid="confirmationSheetConfirm"]').click()
        return True
    else:
        return False


def destroy_block(driver, screen_name):
    """
    destroy_block(driver, screen_name | Str)
    mandatory -> driver
    return | True or False
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    is_blocked = driver.find_element(By.CLASS_NAME,
                                     value='css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr')

    if is_blocked.get_attribute("data-testid").endswith("unblock"):
        driver.implicitly_wait(0.5)
        driver.find_element(By.CLASS_NAME,
                            value="css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr").click()
        driver.implicitly_wait(0.5)
        driver.find_element(By.CLASS_NAME,
                            value="css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-6gpygo.r-peo1c.r-1ps3wis.r-1ny4l3l.r-1udh08x.r-1guathk.r-1udbk01.r-o7ynqc.r-6416eg.r-lrvibr.r-3s2u2q").click()
        return True
    else:
        return False

def create_mute(driver, screen_name):
    """
    create_mute(driver, screen_name | Str)
    mandatory -> driver
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, value='//div[@data-testid="userActions"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.XPATH, value='//div[@data-testid="mute"]').click()


def destroy_mute(driver, screen_name):
    """
    destroy_mute(driver, screen_name | Str)
    mandatory -> driver
    return | True or False
    """
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        driver.find_element(By.XPATH, value='//span[@data-testid="unmuteLink"]')
        driver.find_element(By.XPATH, value='//div[@data-testid="userActions"]').click()
        driver.find_element(By.XPATH, value='//div[@data-testid="mute"]').click()
        return True
    except selenium.common.exceptions.NoSuchElementException:
        print("このユーザーをミュートしていませんでした")
        return False

# ----------------------------------------------------------------------------------------------------------------------