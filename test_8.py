import re
from pyrogram import Client, filters

REG_FILTERS = 'спикер|пройд\wт|регистр|вебинар|митап|лекци|сбор|записыв|демо-урок|семинар|состоится|подборк'

api_id = 2241882
api_hash = "00a1eb9a7425c0bf7f1c4dbad4433572"

app = Client("487616033", api_id, api_hash)

@app.on_message(
    filters.chat(chats=487616033)
    &
    (
    filters.chat(chats=-1001330289823) |
    filters.regex(
        REG_FILTERS,
        flags=re.IGNORECASE)
    )
)
def my_func(app, message):
    if message.text:
        print(message.text)
    if message.caption:
        print(message.caption)

app.run()
