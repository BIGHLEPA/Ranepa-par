from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import SELECTORS
import time


def change_week(driver, amount):

    if amount > 0:
        for _ in range(amount):
            next_week_button = WebDriverWait(driver,10).until(
                    EC.element_to_be_clickable(SELECTORS["next_week_button"])
            )
            next_week_button.click()
            print('Cледующая неделя')
            time.sleep(1)
    elif amount < 0:
        for _ in range(abs(amount)):
            previous_week_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(SELECTORS["previous_week_button"])
            )
            previous_week_button.click()
            print('Предыдущия неделя')
            time.sleep(1)
