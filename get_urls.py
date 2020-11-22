import re
import requests


def get_urls_from_message(message_entities):
    """
    Получить список "вшитых" по тексту сообщения ссылок вместе с title
    соответствущих страниц.
    """
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
        return '\nнет'
    
    list_of_urls = "\n".join(list_of_urls)
    
    return f'\n{list_of_urls}'
