from pyrogram import Client

api_id = 2241882
api_hash = "00a1eb9a7425c0bf7f1c4dbad4433572"

app = Client("487616033", api_id, api_hash)

with Client("487616033", api_id, api_hash) as app:
    #  извлекаем конкретное сообщение из канала
    message = app.get_messages(
        chat_id=-1001294635786,
        message_ids=523,
    )


    channel_name = f'**{message.chat.title}**'
    message_link = f'{message.link}\n'
    web_data = f'{message.web_page.title} {message.web_page.display_url}'
    text_m = channel_name + '\n' + message_link + '\n' + web_data
    
    a = message.caption or message.web_page
    print(message.caption_entities)
