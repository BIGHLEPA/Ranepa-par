
from config import USERDATA
from selenium.webdriver.support.ui import WebDriverWait
from auth import auth
import time



def schedule_finder(driver):
    try:
        driver.get(USERDATA['schedule_url'])
        print('Редирект')
        return True

    except Exception as e:
        print(f"Ошибка: {e}")