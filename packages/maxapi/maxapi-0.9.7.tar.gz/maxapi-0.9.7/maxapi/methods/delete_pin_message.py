from typing import TYPE_CHECKING

from ..methods.types.deleted_pin_message import DeletedPinMessage

from ..enums.http_method import HTTPMethod
from ..enums.api_path import ApiPath

from ..connection.base import BaseConnection


if TYPE_CHECKING:
    from ..bot import Bot


class DeletePinMessage(BaseConnection):
    
    """
    Класс для удаления закреплённого сообщения в чате через API.
    
    https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin

    Attributes:
        bot (Bot): Экземпляр бота для выполнения запроса.
        chat_id (int): Идентификатор чата, из которого нужно удалить закреплённое сообщение.
    """
    
    def __init__(
            self,
            bot: 'Bot',
            chat_id: int,
        ):
            self.bot = bot
            self.chat_id = chat_id

    async def fetch(self) -> DeletedPinMessage:
        
        """
        Выполняет DELETE-запрос для удаления закреплённого сообщения.

        Returns:
            DeletedPinMessage: Результат операции удаления закреплённого сообщения.
        """
        
        if self.bot is None:
            raise RuntimeError('Bot не инициализирован')
        
        return await super().request(
            method=HTTPMethod.DELETE, 
            path=ApiPath.CHATS + '/' + str(self.chat_id) + ApiPath.PIN,
            model=DeletedPinMessage,
            params=self.bot.params,
        )