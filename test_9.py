from os import getenv
import re
import requests

from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')

REG_FILTERS = (
               # ключевые слова по виду мероприятия
               r'вебинар|демо-урок|конференц|лекци|мастер-класс|'
               r'митап|семинар|хакатон|'
               # ключевые слова для подборок меропритий
               r'подборк|'
               # ключевые слова по участникам
               r'спикер|'
               # ключевые слова по действиям
               r'записыв|пройд\wт|регистр\w+|сбор\b|состоится|старт'
            )

QA_EVENTS = -1001299456321
IT_EVENTS_RU = -1001276513255
EPAM_TRAINING_CENTER = -1001343333666
GAMEDEV = -1001171604601
COUNT0_DIGEST = -1001103488303
KARPOV_COURSES = -1001430200876
DATA_EVENTS = -1001294635786
WEBSTANDARDS_EVENTS = -1001389946197
ANALYST_EVENTS = -1001412167674
QA_COURSES_ANNOUNCE = -1001266517876
MOS_EVENTS = -1001077515936
IT_MEETING = -1001426821707

RBC = -1001009291094
INTERFAX = -1001149896996
CODE = -1001448520706

ME = 487616033

CHATS = [
    QA_EVENTS,
    IT_EVENTS_RU,
    EPAM_TRAINING_CENTER,
    GAMEDEV,
    COUNT0_DIGEST,
    KARPOV_COURSES,
    DATA_EVENTS,
    WEBSTANDARDS_EVENTS,
    ANALYST_EVENTS,
    QA_COURSES_ANNOUNCE,
    MOS_EVENTS,
    IT_MEETING,
    RBC,
    INTERFAX,
    CODE,
    ME,
]

def get_urls_from_message(message_entities):
    list_of_urls = []
    for message_entity in message_entities:
        if (
            message_entity['url'] and 
            not message_entity['url'].endswith(('.jpg', '.jpeg'))
        ):
            url = message_entity['url']
            r = requests.get(url)
            page_title = re.search(
                '<\W*title\W*(.*)</title',
                r.text,
                re.IGNORECASE
            ).group(1)
            list_of_urls.append(f'{page_title} - {url}')
    if not list_of_urls:
        return 'нет'
    list_of_urls = "\n".join(list_of_urls)
    return f'\n{list_of_urls}'


app = Client(str(ME), API_ID, API_HASH)

@app.on_message(
    filters.chat(chats=CHATS)
    & 
    (filters.text | filters.caption)
    &
    ~filters.edited
    &
    filters.regex(
        REG_FILTERS,
        flags=re.IGNORECASE)
    )
def my_func(app, message):
    if message.text:
        text_message = str(message.text)
        if message.entities:
            urls_from_message = get_urls_from_message(message.entities)
        else:
            urls_from_message = ''
    else:
        text_message = str(message.caption)
        if message.caption_entities:
            urls_from_message = get_urls_from_message(message.caption_entities)
        else:
            urls_from_message = 'нет'

    # channel_name = message.chat.title
    text_message = text_message.split('\n')
    message_link = message.link

    text = (
        '**EPAM Training Center Belarus**' + '\n' +
        message_link + '\n\n' +
        '\n'.join(text_message[:int(len(text_message)/3)]) +
        '\n'.join(text_message[-int(len(text_message)/3):]) + '\n\n' +
        '**"Зашитые" ссылки**' +
        urls_from_message
    )

    app.send_message(
        chat_id=ME,
        text = text,
        disable_web_page_preview = True,
    )

app.run()
