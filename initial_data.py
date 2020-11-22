"""
Регулярные выражения для фильтрации текстов и подписей
сообщений, поступающих из каналов.
"""
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

"""
ID каналов - источников сообщений о событиях.
"""

"""
QA-каналы
"""
# QA - Анонсы курсов и мероприятий
QA_COURSES_ANNOUNCE = -1001266517876
# QA Events
QA_EVENTS = -1001299456321

"""
DS-каналы
"""
# Data online events & Moscow meetups
DATA_EVENTS = -1001294635786

"""
Каналы для аналитиков
"""
# Analyst Events & Stuff
ANALYST_EVENTS = -1001412167674

"""
Игровая индустрия
"""
# Календарь событий игровой индустрии
GAMEDEV = -1001171604601

"""
Фронтэнд
"""
# События по фронтенду
WEBSTANDARDS_EVENTS = -1001389946197

"""
Каналы универсальной тематики
"""
# Пятничный деплой
COUNT0_DIGEST = -1001103488303
# EPAM Training Center Belarus
EPAM_TRAINING_CENTER = -1001343333666
# IT Events RU
IT_EVENTS_RU = -1001276513255
# IT Meeting - митапы, конференции, тренинги по разработке
IT_MEETING = -1001426821707
# Karpov Courses
KARPOV_COURSES = -1001430200876
# Мероприятия Москвы
MOS_EVENTS = -1001077515936

"""
Общий список каналов для включения в фильтр по источникам сообщений.
"""
CHATS = [
    ANALYST_EVENTS,
    COUNT0_DIGEST,
    DATA_EVENTS,
    EPAM_TRAINING_CENTER,
    GAMEDEV,
    IT_EVENTS_RU,
    IT_MEETING,
    KARPOV_COURSES,
    MOS_EVENTS,
    QA_EVENTS,
    QA_COURSES_ANNOUNCE,
    WEBSTANDARDS_EVENTS,
]
