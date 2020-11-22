import requests, re

f = [
    {
        "_": "MessageEntity",
        "type": "text_link",
        "offset": 0,
        "length": 2,
        "url": "https://telegra.ph/file/1d7b5f64c660914b6efdf.jpg"
    },
    {
        "_": "MessageEntity",
        "type": "bold",
        "offset": 28,
        "length": 65
    },
    {
        "_": "MessageEntity",
        "type": "bold",
        "offset": 316,
        "length": 7
    },
    {
        "_": "MessageEntity",
        "type": "bold",
        "offset": 712,
        "length": 9
    },
    {
        "_": "MessageEntity",
        "type": "text_link",
        "offset": 992,
        "length": 18,
        "url": "https://bit.ly/3pFeF4W"
    }
]


def get_urls_from_message(message_entities):
    list_of_urls = []
    for message_entity in message_entities:
        if (
            message_entity.get('url') and 
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
            list_of_urls = "\n".join(list_of_urls)
    return f'Ссылки из сообщения:\n{list_of_urls}'

print(get_urls_from_message(f))