from __future__ import annotations
from typing import TYPE_CHECKING, Any, Dict, Optional

from ..methods.types.sended_callback import SendedCallback

from ..enums.http_method import HTTPMethod
from ..enums.api_path import ApiPath

from ..connection.base import BaseConnection


if TYPE_CHECKING:
    from ..bot import Bot
    from ..types.message import Message


class SendCallback(BaseConnection):
    
    """
    Класс для отправки callback-ответа с опциональным сообщением и уведомлением.
    
    https://dev.max.ru/docs-api/methods/POST/answers

    Attributes:
        bot (Bot): Экземпляр бота.
        callback_id (str): Идентификатор callback.
        message (Optional[Message]): Сообщение для отправки.
        notification (Optional[str]): Текст уведомления.
    """
    
    def __init__(
            self,
            bot: 'Bot',
            callback_id: str,
            message: Optional[Message] = None,
            notification: Optional[str] = None
        ):
            self.bot = bot
            self.callback_id = callback_id
            self.message = message
            self.notification = notification

    async def fetch(self) -> SendedCallback:
        
        """
        Выполняет POST-запрос для отправки callback-ответа.

        Возвращает результат отправки.

        Returns:
            SendedCallback: Объект с результатом отправки callback.
        """
        
        if self.bot is None:
            raise RuntimeError('Bot не инициализирован')
        
        params = self.bot.params.copy()

        params['callback_id'] = self.callback_id

        json: Dict[str, Any] = {}
        
        if self.message: 
            json['message'] = self.message.model_dump()
        if self.notification: 
            json['notification'] = self.notification

        return await super().request(
            method=HTTPMethod.POST, 
            path=ApiPath.ANSWERS,
            model=SendedCallback,
            params=params,
            json=json
        )