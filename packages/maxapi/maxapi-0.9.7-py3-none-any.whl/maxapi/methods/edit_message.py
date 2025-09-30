from __future__ import annotations
import asyncio

from ..types.errors import Error
from typing import Any, Dict, List, TYPE_CHECKING, Optional

from ..utils.message import process_input_media

from .types.edited_message import EditedMessage
from ..types.message import NewMessageLink
from ..types.attachments.attachment import Attachment
from ..types.input_media import InputMedia, InputMediaBuffer
from ..enums.parse_mode import ParseMode
from ..enums.http_method import HTTPMethod
from ..enums.api_path import ApiPath

from ..connection.base import BaseConnection
from ..loggers import logger_bot


if TYPE_CHECKING:
    from ..bot import Bot


class EditMessage(BaseConnection):
    
    """
    Класс для редактирования существующего сообщения через API.
    
    https://dev.max.ru/docs-api/methods/PUT/messages

    Attributes:
        bot (Bot): Экземпляр бота для выполнения запроса.
        message_id (str): Идентификатор сообщения для редактирования.
        text (Optional[str]): Новый текст сообщения.
        attachments (Optional[List[Attachment | InputMedia | InputMediaBuffer]]): 
            Список вложений для сообщения.
        link (Optional[NewMessageLink]): Связь с другим сообщением (например, ответ или пересылка).
        notify (Optional[bool]): Отправлять ли уведомление о сообщении. По умолчанию True.
        parse_mode (Optional[ParseMode]): Формат разметки текста (например, Markdown, HTML).
    """
    
    def __init__(
            self,
            bot: Bot,
            message_id: str,
            text: Optional[str] = None,
            attachments: Optional[List[Attachment | InputMedia | InputMediaBuffer]] = None,
            link: Optional[NewMessageLink] = None,
            notify: Optional[bool] = None,
            parse_mode: Optional[ParseMode] = None
        ):

            if text is not None and not (len(text) < 4000):
                raise ValueError('text должен быть меньше 4000 символов')
        
            self.bot = bot
            self.message_id = message_id
            self.text = text
            self.attachments = attachments
            self.link = link
            self.notify = notify
            self.parse_mode = parse_mode

    async def fetch(self) -> Optional[EditedMessage | Error]:
        
        """
        Выполняет PUT-запрос для обновления сообщения.

        Формирует тело запроса на основе переданных параметров и отправляет запрос к API.

        Returns:
            EditedMessage: Обновлённое сообщение.
        """
        
        if self.bot is None:
            raise RuntimeError('Bot не инициализирован')
        
        params = self.bot.params.copy()

        json: Dict[str, Any] = {'attachments': []}

        params['message_id'] = self.message_id

        if self.text is not None: 
            json['text'] = self.text
        
        if self.attachments:
            
            for att in self.attachments:

                if isinstance(att, InputMedia) or isinstance(att, InputMediaBuffer):
                    input_media = await process_input_media(
                        base_connection=self,
                        bot=self.bot,
                        att=att
                    )
                    json['attachments'].append(
                        input_media.model_dump()
                    ) 
                else:
                    json['attachments'].append(att.model_dump()) 
                    
        if self.link is not None: 
            json['link'] = self.link.model_dump()
        if self.notify is not None: 
            json['notify'] = self.notify
        if self.parse_mode is not None: 
            json['format'] = self.parse_mode.value

        await asyncio.sleep(self.bot.after_input_media_delay)
        
        response = None
        for attempt in range(self.ATTEMPTS_COUNT):
            response = await super().request(
                method=HTTPMethod.PUT, 
                path=ApiPath.MESSAGES,
                model=EditedMessage,
                params=params,
                json=json
            )

            if isinstance(response, Error):
                if response.raw.get('code') == 'attachment.not.ready':
                    logger_bot.info(f'Ошибка при отправке загруженного медиа, попытка {attempt+1}, жду {self.RETRY_DELAY} секунды')
                    await asyncio.sleep(self.RETRY_DELAY)
                    continue
            
            return response
        return response