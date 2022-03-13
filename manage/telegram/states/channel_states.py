from aiogram.utils.helper import Helper, HelperMode, ListItem


class ChannelStates(Helper):
    """ Состояния для режима работы с каналами """

    mode = HelperMode.snake_case

    ADD = ListItem()
    DELETE = ListItem()
