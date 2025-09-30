from typing import Optional

from ....enums.button_type import ButtonType

from .button import Button


class LinkButton(Button):
    
    """
    Кнопка с внешней ссылкой.
    
    Args:
        url: Ссылка для перехода (должна содержать http/https)
    """

    type: ButtonType = ButtonType.LINK
    url: Optional[str] = None