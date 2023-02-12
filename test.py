from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import selenium

options = Options()
options.add_argument(f"--user-data-dir=C:/Users/yuich/AppData/Local/Google/Chrome/User Data/profiledata")
options.add_argument(f"--profile-directory=Profile 2")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def is_Private(screen_name):
    driver.get(f"https://twitter.com/{screen_name}")
    driver.implicitly_wait(1)
    try:
        is_private = driver.find_element(By.XPATH,value='//*[@data-testid="icon-lock"]')
        if is_private:
            print("鍵アカウントです")
            return True
    except selenium.common.exceptions.NoSuchElementException:
        print("公開アカウントです")
        return False


is_Private("RIMU__RINU__")