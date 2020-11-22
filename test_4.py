from datetime import datetime as dt

from pyrogram import Client, filters

api_id = 2241882
api_hash = "00a1eb9a7425c0bf7f1c4dbad4433572"

app = Client("487616033", api_id, api_hash)

filters.chat(chats=487616033)

@app.on_message()
def my_func(app, message):
    print(f'{message.chat.title}: {message.chat.id}')
    # print(f'{message.forward_from_chat.title}: {message.forward_from_chat.id}')
    # print(message.link)
    # message.forward('me')

app.run()
