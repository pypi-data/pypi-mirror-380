from typing import TYPE_CHECKING, Optional

from .update import Update

from ...types.users import User

if TYPE_CHECKING:
    from ...bot import Bot
    

class BotAdded(Update):
    
    """
    Обновление, сигнализирующее о добавлении бота в чат.

    Attributes:
        chat_id (int): Идентификатор чата, куда добавлен бот.
        user (User): Объект пользователя-бота.
        is_channel (bool): Указывает, был ли бот добавлен в канал или нет
    """
    
    chat_id: int
    user: User
    is_channel: bool
    
    if TYPE_CHECKING:
        bot: Optional[Bot]

    def get_ids(self):
        return (self.chat_id, self.user.user_id)