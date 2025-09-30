from typing import TYPE_CHECKING, Optional

from .update import Update

from ...types.users import User

if TYPE_CHECKING:
    from ...bot import Bot


class BotStopped(Update):
    
    """
    Обновление, сигнализирующее об остановке бота.

    Attributes:
        chat_id (int): Идентификатор чата.
        user (User): Пользователь (бот).
        user_locale (Optional[str]): Локаль пользователя.
        payload (Optional[str]): Дополнительные данные.
    """
    
    chat_id: int
    user: User
    user_locale: Optional[str] = None
    payload: Optional[str] = None
    
    if TYPE_CHECKING:
        bot: Optional[Bot]

    def get_ids(self):
        return (self.chat_id, self.user.user_id)