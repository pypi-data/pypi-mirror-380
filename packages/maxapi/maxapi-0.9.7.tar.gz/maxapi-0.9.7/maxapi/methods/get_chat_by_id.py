from typing import TYPE_CHECKING

from ..types.chats import Chat

from ..enums.http_method import HTTPMethod
from ..enums.api_path import ApiPath

from ..connection.base import BaseConnection


if TYPE_CHECKING:
    from ..bot import Bot


class GetChatById(BaseConnection):

    """
    Класс для получения информации о чате по его идентификатору.
    
    https://dev.max.ru/docs-api/methods/GET/chats/-chatId-

    Attributes:
        bot (Bot): Экземпляр бота для выполнения запроса.
        id (int): Идентификатор чата.
    """
    
    def __init__(
            self, 
            bot: 'Bot',
            id: int
        ):
        self.bot = bot
        self.id = id

    async def fetch(self) -> Chat:
        
        """
        Выполняет GET-запрос для получения данных чата.

        Returns:
            Chat: Объект чата с полной информацией.
        """
        
        if self.bot is None:
            raise RuntimeError('Bot не инициализирован')
        
        return await super().request(
            method=HTTPMethod.GET, 
            path=ApiPath.CHATS.value + '/' + str(self.id),
            model=Chat,
            params=self.bot.params
        )