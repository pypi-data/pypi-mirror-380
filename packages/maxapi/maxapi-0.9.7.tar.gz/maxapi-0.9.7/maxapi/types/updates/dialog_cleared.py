from typing import TYPE_CHECKING, Optional

from .update import Update

from ...types.users import User

if TYPE_CHECKING:
    from ...bot import Bot


class DialogCleared(Update):
    
    """
    Обновление, сигнализирующее об очистке диалога с ботом.

    Attributes:
        chat_id (int): Идентификатор чата.
        user (User): Пользователь (бот).
        user_locale (Optional[str]): Локаль пользователя.
    """
    
    chat_id: int
    user: User
    user_locale: Optional[str] = None
    
    if TYPE_CHECKING:
        bot: Optional[Bot]

    def get_ids(self):
        return (self.chat_id, self.user.user_id)