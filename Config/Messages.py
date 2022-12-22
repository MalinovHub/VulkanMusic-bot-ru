from Config.Singleton import Singleton
from Config.Configs import VConfigs
from Config.Emojis import VEmojis


class Messages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.__emojis = VEmojis()
            configs = VConfigs()
            self.STARTUP_MESSAGE = 'Запускаю Гефест...'
            self.STARTUP_COMPLETE_MESSAGE = 'Гефест уже работает.'

            self.SONGINFO_UPLOADER = "Uploader: "
            self.SONGINFO_DURATION = "Duration: "
            self.SONGINFO_REQUESTER = 'Requester: '
            self.SONGINFO_POSITION = 'Position: '

            self.SONGS_ADDED = 'Загрузка `{}` песен для добавления в очередь'
            self.SONG_ADDED = 'Скачивание песни `{}` для добавления в очередь'
            self.SONG_ADDED_TWO = f'{self.__emojis.MUSIC} Песня добавлена ​​в очередь'
            self.SONG_PLAYING = f'{self.__emojis.MUSIC} Сейчас играет песня'
            self.SONG_PLAYER = f'{self.__emojis.MUSIC} Проигрыватель песен'
            self.QUEUE_TITLE = f'{self.__emojis.MUSIC} Песни в очереди'
            self.ONE_SONG_LOOPING = f'{self.__emojis.MUSIC} Зацикливание одной песни'
            self.ALL_SONGS_LOOPING = f'{self.__emojis.MUSIC} Зацикливание всех песен'
            self.SONG_PAUSED = f'{self.__emojis.PAUSE} Песня приостановлена'
            self.SONG_RESUMED = f'{self.__emojis.PLAY} Играет песня'
            self.SONG_SKIPPED = f'{self.__emojis.SKIP} Песня пропущена'
            self.RETURNING_SONG = f'{self.__emojis.BACK} Воспроизведение предыдущей песни'
            self.STOPPING = f'{self.__emojis.STOP} Игрок остановлен'
            self.EMPTY_QUEUE = f'{self.__emojis.QUEUE} Очередь песен пуста, используйте {configs.BOT_PREFIX}play, чтобы добавить новые песни'
            self.SONG_DOWNLOADING = f'{self.__emojis.DOWNLOADING} Загрузка...'
            self.PLAYLIST_CLEAR = f'{self.__emojis.MUSIC} Плейлист теперь пуст'

            self.HISTORY_TITLE = f'{self.__emojis.MUSIC} Проигранные песни'
            self.HISTORY_EMPTY = f'{self.__emojis.QUEUE} В истории нет музыки'

            self.SONG_MOVED_SUCCESSFULLY = 'Песня `{}` с позиции `{}` успешно перемещена на позицию `{}`'
            self.SONG_REMOVED_SUCCESSFULLY = 'Песня `{}` успешно удалена'
            self.LOOP_ALL_ON = f'{self.__emojis.ERROR} Гефест зацикливает все песни, используйте {configs.BOT_PREFIX}loop off, чтобы сначала отключить этот цикл'
            self.LOOP_ONE_ON = f'{self.__emojis.ERROR} Гефест зацикливает одну песню, используйте {configs.BOT_PREFIX}loop off, чтобы сначала отключить этот цикл'
            self.LOOP_ALL_ALREADY_ON = f'{self.__emojis.LOOP_ALL} Гефест уже зацикливает все песни'
            self.LOOP_ONE_ALREADY_ON = f'{self.__emojis.LOOP_ONE} Гефест уже зацикливает текущую песню'
            self.LOOP_ALL_ACTIVATE = f'{self.__emojis.LOOP_ALL} Зацикливание всех песен'
            self.LOOP_ONE_ACTIVATE = f'{self.__emojis.LOOP_ONE} Зацикливание текущей песни'
            self.LOOP_DISABLE = f'{self.__emojis.LOOP_OFF} Цикл отключен'
            self.LOOP_ALREADY_DISABLE = f'{self.__emojis.ERROR} Цикл уже отключен'
            self.LOOP_ON = f'{self.__emojis.ERROR} Эта команда не может быть вызвана с любой активированной петлей. Используйте {configs.BOT_PREFIX}loop off, чтобы отключить цикл.'
            self.BAD_USE_OF_LOOP = f"""{self.__emojis.ERROR} Недопустимые аргументы команды Loop. Используйте цикл справки {configs.BOT_PREFIX} для получения дополнительной информации.
                                -> Доступные аргументы: ["all", "off", "one", ""]"""

            self.SONGS_SHUFFLED = f'{self.__emojis.SHUFFLE} Песни успешно перемешаны'
            self.ERROR_SHUFFLING = f'{self.__emojis.ERROR} Ошибка при перемешивании песен'
            self.ERROR_MOVING = f'{self.__emojis.ERROR} Ошибка при перемещении песен'
            self.LENGTH_ERROR = f'{self.__emojis.ERROR} Числа должны быть между 1 и длиной очереди, используйте -1 для последней песни'
            self.ERROR_NUMBER = f'{self.__emojis.ERROR} Для этой команды требуется число'
            self.ERROR_PLAYING = f'{self.__emojis.ERROR} Ошибка при воспроизведении песен'
            self.COMMAND_NOT_FOUND = f'{self.__emojis.ERROR} Команда не найдена, введите {configs.BOT_PREFIX}help, чтобы увидеть все команды'
            self.UNKNOWN_ERROR = f'{self.__emojis.ERROR} Неизвестная ошибка, при необходимости используйте {configs.BOT_PREFIX}reset для сброса плеера вашего сервера'
            self.ERROR_MISSING_ARGUMENTS = f'{self.__emojis.ERROR} В этой команде отсутствуют аргументы. Введите {configs.BOT_PREFIX}help "command", чтобы увидеть больше информации об этой команде.'
            self.NOT_PREVIOUS = f'{self.__emojis.ERROR} Нет предыдущей песни для воспроизведения'
            self.PLAYER_NOT_PLAYING = f'{self.__emojis.ERROR} Песня не воспроизводится. Используйте {configs.BOT_PREFIX}play, чтобы запустить проигрыватель.'
            self.IMPOSSIBLE_MOVE = 'Это невозможно :('
            self.ERROR_TITLE = 'Ошибка :-('
            self.COMMAND_NOT_FOUND_TITLE = 'Это странно :-('
            self.NO_CHANNEL = 'Чтобы воспроизвести музыку, сначала подключитесь к любому голосовому каналу.'
            self.NO_GUILD = f'На этом сервере нет игрока, попробуйте {configs.BOT_PREFIX}сбросить'
            self.INVALID_INPUT = f'Этот URL слишком странный, попробуйте что-нибудь получше или введите {configs.BOT_PREFIX}help play'
            self.INVALID_INDEX = f'В качестве аргумента передан недопустимый индекс.'
            self.INVALID_ARGUMENTS = f'Команде переданы недопустимые аргументы.'
            self.DOWNLOADING_ERROR = f"{self.__emojis.ERROR} Невозможно загрузить и воспроизвести это видео"
            self.EXTRACTING_ERROR = f'{self.__emojis.ERROR} Произошла ошибка при поиске песен.'

            self.ERROR_IN_PROCESS = f"{self.__emojis.ERROR} Из-за внутренней ошибки ваш плеер был перезапущен, песня пропущена."
            self.MY_ERROR_BAD_COMMAND = 'Эта строка служит для проверки того, не была ли какая-то ошибка вызвана мной намеренно'
            self.BAD_COMMAND_TITLE = 'Неправильное использование команды'
            self.BAD_COMMAND = f'{self.__emojis.ERROR} Неправильное использование этой команды, введите {configs.BOT_PREFIX}help "command", чтобы лучше понять команду'
            self.VIDEO_UNAVAILABLE = f'{self.__emojis.ERROR} Извините. Это видео недоступно для скачивания».'
            self.ERROR_DUE_LOOP_ONE_ON = f'{self.__emojis.ERROR} Эта команда не может быть выполнена с активированным циклом один. Используйте {configs.BOT_PREFIX}loop off, чтобы отключить цикл.'


class SearchMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = VConfigs()
            self.UNKNOWN_INPUT = f'Этот тип ввода был слишком странным, попробуйте что-нибудь другое или введите {config.BOT_PREFIX}help play'
            self.UNKNOWN_INPUT_TITLE = 'Ничего не найдено'
            self.GENERIC_TITLE = 'URL не может быть обработан'
            self.SPOTIFY_NOT_FOUND = 'Spotify не удалось обработать ни одну песню с этим входом, проверьте ссылку или повторите попытку позже.'
            self.YOUTUBE_NOT_FOUND = 'Youtube не может обработать ни одну песню с этим входом, проверьте ссылку или повторите попытку позже.'
            self.DEEZER_NOT_FOUND = 'Deezer не удалось обработать ни одну песню с этим входом, проверьте ссылку или повторите попытку позже.'


class SpotifyMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_SPOTIFY_URL = 'Недействительный URL-адрес Spotify, проверьте свою ссылку.'
            self.GENERIC_TITLE = 'URL не может быть обработан'


class DeezerMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_DEEZER_URL = 'Недействительный URL-адрес Deezer, проверьте свою ссылку.'
            self.GENERIC_TITLE = 'URL не может быть обработан'
