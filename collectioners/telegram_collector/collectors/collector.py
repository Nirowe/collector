from typing import Protocol


class Collector(Protocol):
    """
    Класс для сбора данных c площадок
    :param
    """

    def __init__(self, client):
        self._server = server

    def process(self, data):
        """ Обрабатывает публикацию и отправляет на server """
        item = self._process_item(data)
        self._server.send()

    def _process_item(self, data):
        raise NotImplementedError

