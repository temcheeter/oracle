from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from io import BytesIO
import textwrap
import pytz
import json


def predict(predict_date: str):
    img = Image.open('source.png')
    idraw = ImageDraw.Draw(img)
    headline = ImageFont.truetype('century_bold.ttf', size=90)
    forecast = ImageFont.truetype('century_regular.ttf', size=48)
    dateline = ImageFont.truetype('Segoe-UI-Variable-Static-Text-Semibold.ttf', size=42)
    dash = ImageFont.truetype('Segoe-UI-Variable-Static-Text-Semibold.ttf', size=48)

    with open('forecasts.json', 'r', encoding='utf-8') as f:
        dictionary = json.load(f)
        text = dictionary[predict_date]
        wrapped_text = textwrap.fill(text, width=20)
    time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M')
    time = time[:-1] + str(int(time[-1]) + 9)[-1]
    date = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d.%m')

    idraw.text((414, 500), predict_date, 'black', font=headline, anchor='mm')
    idraw.text((420, 780), wrapped_text, font=forecast, fill='#33273c', anchor='mm')
    idraw.text((218, 1743), date, font=dateline, anchor='rm')
    idraw.text((15, 1743), time, font=dateline, anchor='lm')
    idraw.text((123, 1738), '|', 'grey', font=dash, anchor='mm')

    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    return img_bytes