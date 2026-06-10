from selenium.webdriver.common.by import By
USERDATA = {
    "login": 'no',
    'password': 'no',
    'url': 'https://my.ranepa.ru/student/login',
    'schedule_url': "https://my.ranepa.ru/lk/student/schedule"
}
SELECTORS = {
    'login_field': (By.ID, "login"),
    'password_field': (By.ID, 'password'),
    'enter_button': (By.CLASS_NAME, "main-button--primary"),
    'next_week_button': (By.CLASS_NAME, 'box-schedule__button--next'),
    'previous_week_button': (By.CLASS_NAME, 'box-schedule__button--prev')
}
BLOCK_PIECES = {
    'name_element': ('card-schedule__title'),
    'time_element': ("card-schedule__time"),
    'type_element': ("card-schedule__type"),
    'place_element': ('card-schedule__address'),
    'date_block': ('box-schedule__table-head'),
    'day_columns': ('vuecal__cell-content'),
    'lesson_blocks': ('vuecal__event')
}
