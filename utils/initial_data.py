
class InitialData:
    
    def __init__(self):
        
        self.qa_events = -1001299456321
        self.qa_courses_announce = -1001266517876
        self.data_events = -1001294635786
        self.analyst_events = -1001412167674
        self.gamedev = -1001171604601
        self.webstandards_events = -1001389946197
        self.count0_digest = -1001103488303
        self.epam_training_center = -1001343333666
        self.it_events_ru = -1001276513255
        self.it_meeting = -1001426821707
        self.karpov_courses = -1001430200876
        self.mos_events = -1001077515936

    @property
    def qa_channels(self):
        channels = [
            self.qa_events,
            self.qa_courses_announce
        ]
        return channels

    @property
    def ds_channels(self):
        channels = [
            self.data_events
        ]
        return channels
    
    @property
    def analyst_channels(self):
        channels = [
            self.analyst_events
        ]
        return channels
    
    @property
    def gamedev_channels(self):
        channels = [
            self.gamedev
        ]
        return channels
    
    @property
    def frontend_channels(self):
        channels = [
            self.webstandards_events
        ]
        return channels

    @property
    def universal_channels(self):
        channels = [
            self.count0_digest,
            self.epam_training_center,
            self.it_events_ru,
            self.it_meeting,
            self.karpov_courses,
            self.mos_events,
        ]
        return channels
    
    @property
    def chats(self):
        """
        Общий список каналов для включения в фильтр по источникам сообщений.
        """
        channels = [
            self.qa_events,
            self.qa_courses_announce,
            self.data_events,
            self.analyst_events,
            self.gamedev,
            self.webstandards_events,
            self.count0_digest,
            self.epam_training_center,
            self.it_events_ru,
            self.it_meeting,
            self.karpov_courses,
            self.mos_events
        ]
        return channels
    
    @property
    def req_filter(self):
        """
        Регулярные выражения для фильтрации текстов и подписей
        сообщений, поступающих из каналов.
        """
        return (
            # ключевые слова по виду мероприятия
            r'вебинар|демо-урок|конференц|лекци|мастер-класс|баттл|'
            r'митап|семинар|хакатон|выставк|форум|воркшоп|встреча|'
            
            # ключевые слова для подборок мероприятий
            r'подборк|'
            
            # ключевые слова по участникам
            r'спикер|'
            
            # ключевые слова по действиям
            r'записыв|пройд\wт|регистр\w+|сбор\b|состоится|старт|расписан'
        )
