from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from io import BytesIO
from calendar import month_name
import textwrap
from pytz import timezone
import json


def time_n_date():
    month_list = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
                  'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
    month = month_list[datetime.now(timezone('Europe/Moscow')).month - 1]
    year = str(datetime.now(timezone('Europe/Moscow')).year)
    day = str(datetime.now(timezone('Europe/Moscow')).day)
    date = day + ' ' + month + ' ' + year
    time = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M')
    time = time[:-1] + str(int(time[-1]) + 9)[-1]
    return date, time


async def predict(predict_date: str):
    img = Image.open('source.png')
    idraw = ImageDraw.Draw(img)
    headline = ImageFont.truetype('century_bold.ttf', size=90)
    forecast = ImageFont.truetype('century_regular.ttf', size=48)
    dateline = ImageFont.truetype('Segoe-UI-Variable-Static-Text-Semibold.ttf', size=36)
    dash = ImageFont.truetype('Segoe-UI-Variable-Static-Text-Semibold.ttf', size=48)

    with open('forecasts.json', 'r', encoding='utf-8') as f:
        dictionary = json.load(f)
        text = dictionary[predict_date]
        wrapped_text = textwrap.fill(text, width=23)
    date, time = time_n_date()

    idraw.text((414, 500), predict_date, 'black', font=headline, anchor='mm')
    idraw.text((360, 780), wrapped_text, font=forecast, fill='#33273c', anchor='mm')
    idraw.text((15, 1745), date, font=dateline, anchor='lm')
    idraw.text((400, 1745), time, font=dateline, anchor='rm')

    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    return img_bytes
