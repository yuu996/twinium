from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import SessionNotCreatedException
import selenium
import time

options = Options()
options.add_argument(f"--user-data-dir=C:/Users/<username>/AppData/Local/Google/Chrome/User Data/profiledata")
options.add_argument(f"--profile-directory=Profile 2")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def get_followers(screen_name):
    """
    get_followers(screen_name)
    return follower_list
    Failed -> False
    """
    try:
        driver.get(f"https://twitter.com/{screen_name}/followers")
        driver.implicitly_wait(1)
        follower_list = []
        # Code to goto End of the Page
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

            usernames = driver.find_elements(By.CLASS_NAME,value="css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l")
            for list in usernames:
                follower_list.append(list.get_attribute("href"))
        return follower_list
    except Exception:
        return False
