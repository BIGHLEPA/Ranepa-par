
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import USERDATA, SELECTORS


def auth (driver):
    try:

        # ---Ввод Логина---
        login_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(SELECTORS['login_field'])
        ) 
        login_field.send_keys(USERDATA['login'])
        print('Логин введен успешно')

        # ---Ввод Пароля---
        password_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(SELECTORS['password_field'])
        )
        password_field.send_keys(USERDATA['password'])
        print('Пароль введен')

        # ---Нажатие на "Войти"---
        enter_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(SELECTORS["enter_button"])
        )
        enter_button.click()
        print('Вход нажат')
        
        # ---Ожидание загрузки---
        WebDriverWait(driver,10).until(
            EC.url_changes(USERDATA['url'])
        )
        print('Вход выполнен')


        return True
    except Exception as e:

        print(f'Ошибка: {e}')
        return False