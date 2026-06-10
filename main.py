from selenium import webdriver
from schedule_finder import schedule_finder
from google_calendar_events import google_events
from google_calendar_auth import google_calendar_auth
from auth import auth
from change_week import change_week




import time
driver = webdriver.Chrome()
try:
    schedule_finder(driver)
    auth(driver)
    service = google_calendar_auth()
    time.sleep(1)
    change_week(driver, 0)
    time.sleep(1)
    google_events(driver, service, filename ='page.html')
    
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    driver.quit()

