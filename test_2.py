from datetime import datetime as dt

from pyrogram import Client, filters

api_id = 2241882
api_hash = "00a1eb9a7425c0bf7f1c4dbad4433572"

app = Client("487616033", api_id, api_hash)

@app.on_message()
def my_func(app, message):
    if message.chat.type == 'channel':
        text = '\n'.join(
            [
                'ID поступившего из канала сообщения: ' + f'**{str(message.message_id)}**',
                
                'Дата и время поступления сообщения: ' + f'**{dt.fromtimestamp(message.date).strftime("%d-%m-%H %H:%M:%S")}**',
                
                'Название канала - первоисточника сообщения: ' + f'**{message.forward_from_chat.title}**',

                'ID канала - первоисточника: ' + f'**{message.forward_from_chat.id}**',
                
                'ID сообщения в канале-первоисточнике: ' + f'**{str(message.forward_from_message_id)}**',

                'Название канала, из которого пришло сообщение: ' + f'**{str(message.сhat.id)}**',
            ]
        )
    else:
        text = '\n'.join(
            [
                'ID поступившего сообщения: ' + f'**{str(message.message_id)}**',

                'ID чата, из которого пришло сообщение: ' + f'**{str(message.сhat.id)}**',
                
                'Дата и время поступления сообщения: ' + f'**{dt.fromtimestamp(message.date).strftime("%d-%m-%H %H:%M:%S")}**',
            ]
        )
        
    app.send_message(
        chat_id='me',
        text = text
    )

app.run()  # Automatically start() and idle()
