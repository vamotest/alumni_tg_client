from datetime import datetime as dt

from pyrogram import Client, filters


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


api_id = 2241882
api_hash = '00a1eb9a7425c0bf7f1c4dbad4433572'

app = Client("487616033", api_id, api_hash)


@app.on_message(
    (filters.chat(chats=CHATS))
    & 
    (filters.text | filters.caption)
    &
    ~filters.edited
    
)
def my_func(app, message):
    message_chat_id = str(message.chat.id)
    message_chat_title = str(message.chat.title)

    data_about_message = '\n'.join(
        [
            '**Информация о поступившем сообщении**\n',

            f'Название канала: **{message_chat_title}**',
            f'ID канала: **{message_chat_id}**',
            f'ID сообщения **{str(message.message_id)}**',
            f'Дата и время сообщения: **{dt.fromtimestamp(message.date).strftime("%d-%m-%H %H:%M:%S")}**',
            ]
        )

    if message.forward_from_chat:
        message_fchat_id = str(message.forward_from_chat.id)
        message_fchat_title = str(message.forward_from_chat.title)
        message_fchat_message_id = str(message.forward_from_message_id)
        
        data_about_forwarded_message = '\n'.join(
            [
                '\n**Сообщение было переадресовано**\n',

                f'Название канала - первоисточника: **{message_fchat_title}**',
                f'ID канала: **{message_fchat_id}**',
                f'ID сообщения в канале: **{message_fchat_message_id}**',
            ]
        )
    else:
        data_about_forwarded_message = ''

    if message.chat.type == 'channel':
        message_link = f'Ссылка на сообщение: {message.link}'
    else:
        message_link = ''

    prefix = '**Текст сообщения**\n'

    if message.text:
        text_message = prefix + str(message.text.html)
    else:
        text_message = prefix + str(message.caption.html)

    text = data_about_message + '\n' + data_about_forwarded_message + '\n' + message_link + '\n' + ' '.join(text_message.split('\n')[:10])

    app.send_message(
        chat_id='me',
        text = text,
        disable_web_page_preview = True,
    )


app.run()
