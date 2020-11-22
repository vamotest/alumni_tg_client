import os
import re

from dotenv import load_dotenv
from pyrogram import Client, filters

from get_urls import get_urls_from_message
from utils.initial_data import InitialData

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
ME = os.getenv('ME')
app = Client(ME, API_ID, API_HASH)

initial_data = InitialData()


@app.on_message(
    #  отбираем сообщения из избранных каналов
    filters.chat(chats=initial_data.chats)
    &
    #  отбираем текстовые сообщения + медиасообщения с подписями
    (filters.text | filters.caption)
    &
    #  отсекаем отредактированные сообщения
    ~filters.edited
    &
    #  отбираем сообщения с текстом, проходящим по фильтрам из регулярок
    filters.regex(
        initial_data.req_filter,
        flags=re.IGNORECASE)
)
def get_and_send_filtered_messages(app, message):
    """
    1. Вытащить текст сообщения или текст подписи.
    2. Вытащить "зашитые" ссылки (при наличии) и сформировать из них список.
    3. Составить отформатированное сообщение.
    4. Отправить сообщение в saved_messages.
    """
    text_message = message.text or message.caption
    message_entity = message.entities or message.caption_entities
    
    if message_entity:
        urls_from_message = get_urls_from_message(message_entity)
    else:
        urls_from_message = 'нет'
    
    channel_name = f'**{message.chat.title}**\n'
    text_message_full = str(text_message).split('\n')
    text_message_shortened = (
        '\n'.join(text_message_full[:int(len(text_message) / 3)]) +
        '\n'.join(text_message_full[-int(len(text_message) / 3):]) + '\n\n'
    )
    message_link = message.link + '\n\n'
    
    text = (
        channel_name + message_link + text_message_shortened +
        '**"Зашитые" ссылки**' + urls_from_message
    )
    
    app.send_message(
        chat_id=ME,
        text=text,
        disable_web_page_preview=True,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
