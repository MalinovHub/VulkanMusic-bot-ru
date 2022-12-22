from Config.Singleton import Singleton
from Config.Configs import VConfigs


class Helper(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = VConfigs()
            self.HELP_SKIP = 'Пропустить текущую воспроизводимую песню.'
            self.HELP_SKIP_LONG = 'Пропустить воспроизведение текущей песни, не работает, если активирован первый цикл. \n\nАргументы: нет.'
            self.HELP_RESUME = 'Возобновляет проигрыватель песен.'
            self.HELP_RESUME_LONG = 'Если игрок поставлен на паузу, возобновить воспроизведение. \n\nАргументы: нет.'
            self.HELP_CLEAR = 'Очистить очередь и историю песен.'
            self.HELP_CLEAR_LONG = 'Очистить очередь песен и историю песен. \n\nАргументы: нет.'
            self.HELP_STOP = 'Остановить проигрыватель песен.'
            self.HELP_STOP_LONG = 'Остановите проигрыватель песен, очистите очередь и историю и удалите Гефест из голосового канала.\n\nАргументы: нет.'
            self.HELP_LOOP = 'Управление циклом песен.'
            self.HELP_LOOP_LONG = """Управление циклом песен.\n\n Требование: воспроизводимая песня.\nАргументы:
                One - Начать зацикливание текущей песни.
                All - Начать зацикливание всех песен в очереди.
                Off. - отключить цикл."""
            self.HELP_NP = 'Показать информацию о текущей песне.'
            self.HELP_NP_LONG = 'Показать информацию о воспроизводимой песне.\n\nТребуется: воспроизводимая песня.\nАргументы: нет.'
            self.HELP_QUEUE = f'Показать первые {config.MAX_SONGS_IN_PAGE} песни в очереди.'
            self.HELP_QUEUE_LONG = f'Показать первую {config.MAX_SONGS_IN_PAGE} песню в очереди.\n\nАргументы: нет.'
            self.HELP_PAUSE = 'Приостанавливает проигрыватель песен.'
            self.HELP_PAUSE_LONG = 'При воспроизведении приостанавливает воспроизведение песни.\n\nАргументы: нет'
            self.HELP_PREV = 'Воспроизвести предыдущую песню.'
            self.HELP_PREV_LONG = 'Воспроизвести предыдущую песню. При воспроизведении текущая песня вернется в очередь.\n\nТребуется: отключить цикл.\nАргументы: нет.'
            self.HELP_SHUFFLE = 'Перемешать воспроизводимые песни.'
            self.HELP_SHUFFLE_LONG = 'Случайно перемешать песни в очереди.\n\nАргументы: нет.'
            self.HELP_PLAY = 'Воспроизведение песни с URL-адреса'
            self.HELP_PLAY_LONG = 'Воспроизвести песню в разногласиях. \n\nТребуется: вы должны быть подключены к голосовому каналу.\nАргументы: ссылка на песню/плейлист Youtube, Spotify или Deezer или название песни для поиска на Youtube.'
            self.HELP_HISTORY = f'Показать историю воспроизведенных песен.'
            self.HELP_HISTORY_LONG = f'Показать последние {config.MAX_SONGS_HISTORY} сыгранные песни'
            self.HELP_MOVE = 'Перемещает песню с позиции pos1 на позицию 2 в очереди.'
            self.HELP_MOVE_LONG = 'Перемещает песню с позиции x на позицию y в очереди.\n\nТребуется: обе позиции должны быть допустимыми числами.\nАргументы: 1º номер => исходная позиция, 2º номер => конечная позиция. Оба числа могут быть равны -1 для обозначения последней песни в очереди.\nПо умолчанию: По умолчанию, если второе число не передано, оно будет равно 1, перемещая выбранную песню на позицию 1º.'
            self.HELP_REMOVE = 'Удалить песню с позиции x.'
            self.HELP_REMOVE_LONG = 'Удалить песню из очереди в указанной позиции.\n\nТребуется: Позиция должна быть допустимым числом.\nАргументы: 1º self.Number => Позиция песни в очереди.'
            self.HELP_RESET = 'Сбросить проигрыватель сервера.'
            self.HELP_RESET_LONG = 'Сбросить проигрыватель сервера. Рекомендуется, если вы обнаружите ошибку любого типа.\n\nАргументы: Нет'
            self.HELP_HELP = f'Используйте {config.BOT_PREFIX}команду help для получения дополнительной информации.'
            self.HELP_HELP_LONG = f'Используйте справочную команду {config.BOT_PREFIX} для получения дополнительной информации о выбранной команде.'
            self.HELP_INVITE = 'Отправьте URL-адрес приглашения для вызова Гефест на ваш сервер.'
            self.HELP_INVITE_LONG = 'Отправьте сообщение в текстовом канале с URL-адресом, который будет использоваться для приглашения Гефест на ваш собственный сервер.\n\nАргументы: нет.'
            self.HELP_RANDOM = 'Вернуть случайное число от 1 до x.'
            self.HELP_RANDOM_LONG = 'Отправить случайно выбранное число между 1 и числом, которое вы передаете.\n\nНеобходимо: число должно быть допустимым числом.\nАргументы: 1º Любое число для использования в качестве диапазона.'
            self.HELP_CHOOSE = 'Случайно выберите один пройденный предмет.'
            self.HELP_CHOOSE_LONG = 'Выберите случайным образом один элемент, переданный в этой команде.\n\nТребование: Имена должны быть разделены запятой.\nАргументы: столько, сколько хотите.'
            self.HELP_CARA = 'Вернуть cara или coroa.'
            self.HELP_CARA_LONG = 'Вернуть cara или coroa.'

            self.SLASH_QUEUE_DESCRIPTION = f'Количество страниц очереди, только {config.MAX_SONGS_IN_PAGE} музыки на странице'
            self.SLASH_MOVE_HELP = 'Перемещает песню с позиции pos1 на позицию 2 в очереди.'
