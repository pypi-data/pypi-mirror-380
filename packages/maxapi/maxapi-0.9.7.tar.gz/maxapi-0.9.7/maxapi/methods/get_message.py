from typing import TYPE_CHECKING

from ..types.message import Message
from ..enums.http_method import HTTPMethod
from ..enums.api_path import ApiPath
from ..connection.base import BaseConnection


if TYPE_CHECKING:
    from ..bot import Bot


class GetMessage(BaseConnection):
    
    """
    Класс для получения сообщения.
    
    https://dev.max.ru/docs-api/methods/GET/messages/-messageId-

    Attributes:
        bot (Bot): Экземпляр бота для выполнения запроса.
        message_id (Optional[str]): ID сообщения (mid), чтобы получить одно сообщение в чате.
    """
    
    def __init__(
            self,
            bot: 'Bot', 
            message_id: str,
        ):
        self.bot = bot
        self.message_id = message_id

    async def fetch(self) -> Message:
        
        """
        Выполняет GET-запрос для получения сообщения.

        Returns:
            Message: Объект с полученным сообщением.
        """
        
        if self.bot is None:
            raise RuntimeError('Bot не инициализирован')
        
        return await super().request(
            method=HTTPMethod.GET, 
            path=ApiPath.MESSAGES + '/' + self.message_id,
            model=Message,
            params=self.bot.params
        )