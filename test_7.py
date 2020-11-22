from datetime import datetime as dt

from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup

api_id = 2241882
api_hash = '00a1eb9a7425c0bf7f1c4dbad4433572'

# CHAT_ID = -1001300967134



CHAT_ID = -1001330289823 #  Чат нашей группы

RBC = -1001009291094

with Client("487616033", api_id, api_hash) as app:
    count = 0
    for message in app.iter_history(
        chat_id=-1001171604601,
        ):
        if message.text:
            text = str(message.text).lower()
        elif message.caption:
            text = str(message.caption).lower()
        else:
            continue
        if text.find('регистр') != -1:
            count +=1
        
    app.send_message(
                chat_id='me',
                text = count,
                disable_web_page_preview = True,
        )
