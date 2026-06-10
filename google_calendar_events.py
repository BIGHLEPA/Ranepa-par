
from bs4 import BeautifulSoup
from config import BLOCK_PIECES
from datetime import datetime
from google_calendar_auth import google_calendar_auth
from googleapiclient.errors import HttpError
months = {
    'Января': '01', 'Февраля': '02', 'Марта': '03', 'Апреля': '04',
    'Мая': '05', 'Июня': '06', 'Июля': '07', 'Августа': '08',
    'Сентября': '09', 'Октября': '10', 'Ноября': '11', 'Декабря': '12'
}
year = datetime.now().year

event = {
            "summary": "Error",
            "description": "Места нет",
            "colorId": 2,
            "start": {
                'dateTime': "2026-04-01T09:00:00+02:00",
                'timeZone': 'Europe/Moscow'
            },
            "end": {
                'dateTime': "2026-04-01T17:00:00+02:00",
                'timeZone': 'Europe/Moscow'
            }
            }   

def google_events(driver, service, filename ='page.html'):
    full_html = driver.page_source
    soup = BeautifulSoup(full_html, 'html.parser')
    #---ищем даты---
    date_blocks = soup.find_all('div', class_ = BLOCK_PIECES['date_block'])
    #---ищем столбцы---s
    day_columns = soup.find_all('div', class_ = BLOCK_PIECES['day_columns'])
    #---СОЗДАЕМ СПИСОК ЧИСТЫХ ДАТ
    dates = []
    for i in range (len(date_blocks)):
        #1 блок грязной даты
        date_element = date_blocks[i].find('p', class_ = 'box-schedule__table-date')
        if date_element:
            dates.append(date_element.text.strip())
        else:
            dates.append('Нет даты')
    #---СОЗДАЕМ ОТДЕЛЬНЫЕ КАРТОЧКИ
    if day_columns:
        for i in range(len(day_columns)):
            current_column = day_columns[i]
            cards_in_this_column = current_column.find_all('div', class_ = BLOCK_PIECES['lesson_blocks'])
            num_cards = len(cards_in_this_column)
            #Разделяем карточки
            if current_column:
                for j in range(num_cards):
                    current_card = cards_in_this_column[j]
                    #ПИШЕМ ИМЯ
                    name_element = current_card.find('p', class_ = BLOCK_PIECES['name_element'])
                    name_text = name_element.text.strip()
                    event["summary"] = name_text

                    #---сохраняем время
                    time_element = current_card.find('p', class_ = BLOCK_PIECES['time_element'])
                    time_text_full = time_element.text.strip()
                    start_time, end_time = time_text_full.split(' - ')
                    month_number, month_name = dates[i].split(' ')
                    google_time_start = str(year) + "-" + months[month_name] + "-" + month_number.zfill(2) + 'T' + start_time + ':00' + "+03:00"
                    google_time_end = str(year) + "-" + months[month_name] + "-" + month_number.zfill(2) + 'T' + end_time + ':00' + "+03:00"
                    event["start"]["dateTime"] = google_time_start
                    event["end"]["dateTime"] = google_time_end
                    #---сохраняем тип пары
                    type_element = current_card.find('p', class_ = BLOCK_PIECES['type_element'])
                    type_text = type_element.text.strip()
                    #---сохраняем место пары
                    place_element = current_card.find('p', class_ = BLOCK_PIECES['place_element'])
                    place_text = place_element.text.strip()
                    event["description"] = type_text + " " + place_text
                    # ОПРЕДЕЛЯЕМ ЦВЕТ
                    if "СДО" in event["description"]:
                        event["colorId"] = 9  # Красный
                    else:
                        event["colorId"] = 10  # Бирюзовый 
                    # Создаем событие
                    try:
                        created_event = service.events().insert(calendarId="primary", body=event).execute()
                        print('Событие создано')
                    except HttpError as error:
                        print(f' Ошибка при создании события "{event["summary"]}": {error}')
    else:
        print(f'На этой неделе занятий нет')
    return(True)


