from datetime import datetime as dt

from pyrogram import Client


IT_EVENTS_RU = -1001276513255
QA_EVENTS = -1001299456321
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


api_id = 2241882
api_hash = '00a1eb9a7425c0bf7f1c4dbad4433572'

with Client("487616033", api_id, api_hash) as app:
    for message in app.iter_history(
        chat_id=IT_EVENTS_RU,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=QA_EVENTS,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )
    
    for message in app.iter_history(
        chat_id=EPAM_TRAINING_CENTER,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=GAMEDEV,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=COUNT0_DIGEST,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=KARPOV_COURSES,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=DATA_EVENTS,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=WEBSTANDARDS_EVENTS,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=ANALYST_EVENTS,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )


    for message in app.iter_history(
        chat_id=QA_COURSES_ANNOUNCE,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=MOS_EVENTS,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )

    for message in app.iter_history(
        chat_id=IT_MEETING,
        limit=3,
        ):
        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            continue
        channel_name = f'**{message.chat.title}**'
        message_link = f'{message.link}\n'
        text_m = channel_name + '\n' + message_link + '\n' + ' '.join(text.split('\n')[:10])
        app.send_message(
            chat_id='me',
            text = text_m,
            disable_web_page_preview = True,
        )
