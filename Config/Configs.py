import os
from decouple import config
from Config.Singleton import Singleton
from Config.Folder import Folder


class VConfigs(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.BOT_PREFIX = '!'
            try:
                self.BOT_TOKEN = config('')
                self.SPOTIFY_ID = config('')
                self.SPOTIFY_SECRET = config('')
                self.BOT_PREFIX = config('p!')
            except:
                print(
                    '[ОШИБКА] -> Вы должны создать файл .env со всеми необходимыми полями, см. документацию для справки')

            self.CLEANER_MESSAGES_QUANT = 5
            self.ACQUIRE_LOCK_TIMEOUT = 10
            self.QUEUE_VIEW_TIMEOUT = 120
            self.COMMANDS_FOLDER_NAME = 'DiscordCogs'
            self.COMMANDS_PATH = f'{Folder().rootFolder}{self.COMMANDS_FOLDER_NAME}'
            self.VC_TIMEOUT = 300

            self.CHANCE_SHOW_PROJECT = 15
            self.PROJECT_URL = ''
            self.SUPPORTING_ICON = 'https://i.pinimg.com/originals/d6/05/b4/d605b4f8c5d1c6ae20dc353ef9f091bd.png'

            self.MAX_PLAYLIST_LENGTH = 50
            self.MAX_PLAYLIST_FORCED_LENGTH = 5
            self.MAX_SONGS_IN_PAGE = 10
            self.MAX_PRELOAD_SONGS = 15
            self.MAX_SONGS_HISTORY = 15

            self.INVITE_MESSAGE = """Чтобы пригласить Гефест на свой сервер, нажмите [здесь]({}). 
            Или используйте этот прямой URL: {}"""

            self.MY_ERROR_BAD_COMMAND = 'Эта строка служит для проверки того, что какая-то ошибка была вызвана мной намеренно.'
            self.INVITE_URL = 'https://discord.com/api/oauth2/authorize?client_id=1041047211678642247&permissions=2910410566465&scope=bot%20applications.commands'

    def getProcessManager(self):
        return self.__manager

    def setProcessManager(self, newManager):
        self.__manager = newManager
