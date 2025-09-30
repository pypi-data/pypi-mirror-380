<p align="center">
  <a href="https://github.com/love-apples/maxapi"><img src="https://s.iimg.su/s/29/DCvw4dx2HZgFdTcpqGAs6xdnJnvD44r9zLga2GGe.png" alt="MaxAPI"></a>
</p>


<p align="center">
<a href='https://github.com/love-apples/maxapi/wiki'>Документация</a> •
<a href='https://github.com/love-apples/maxapi/tree/main/examples'>Примеры</a> •
<a href='https://max.ru/join/IPAok63C3vFqbWTFdutMUtjmrAkGqO56YeAN7iyDfc8'>MAX Чат</a> •
<a href='https://t.me/maxapi_github'>TG Чат</a>
</p>

<p align="center">
<a href='https://pypi.org/project/maxapi/'>
  <img src='https://img.shields.io/pypi/v/maxapi.svg' alt='PyPI version'>
</a>
<a href='https://pypi.org/project/maxapi/'>
  <img src='https://img.shields.io/pypi/pyversions/maxapi.svg' alt='Python Version'>
</a>
<a href='https://love-apples/maxapi/blob/main/LICENSE'>
  <img src='https://img.shields.io/github/license/love-apples/maxapi.svg' alt='License'>
</a>
</p>

## 📦 Установка из PyPi

Стабильная версия

```bash
pip install maxapi
```

## 🐱‍👤 Установка из GitHub

Свежая версия, возможны баги. Рекомендуется только для ознакомления с новыми коммитами.

```bash
pip install git+https://github.com/love-apples/maxapi.git
```



## 🚀 Быстрый старт

Если вы тестируете бота в чате - не забудьте дать ему права администратора!

### Запуск Polling

Если у бота установлены подписки на Webhook - события не будут приходить при методе `start_polling`. При таком случае удалите подписки на Webhook через [MasterBot](https://web.max.ru/masterbot) или через `await bot.delete_webhook()` перед `start_polling`.

```python
import asyncio
import logging

from maxapi import Bot, Dispatcher
from maxapi.types import BotStarted, Command, MessageCreated

logging.basicConfig(level=logging.INFO)

bot = Bot('тут_ваш_токен')
dp = Dispatcher()

# Ответ бота при нажатии на кнопку "Начать"
@dp.bot_started()
async def bot_started(event: BotStarted):
    await event.bot.send_message(
        chat_id=event.chat_id,
        text='Привет! Отправь мне /start'
    )

# Ответ бота на команду /start
@dp.message_created(Command('start'))
async def hello(event: MessageCreated):
    await event.message.answer(f"Пример чат-бота для MAX 💙")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
```

### Запуск Webhook

Перед запуском бота через Webhook, вам нужно установить дополнительные зависимости (fastapi, uvicorn). Можно это сделать через команду:
```bash
pip install maxapi[webhook]
```

Указан пример простого запуска, для более низкого уровня можете рассмотреть [этот пример](https://github.com/love-apples/maxapi/blob/main/examples/webhook/low_level.py).
```python
import asyncio
import logging

from maxapi import Bot, Dispatcher
from maxapi.types import BotStarted, Command, MessageCreated

logging.basicConfig(level=logging.INFO)

bot = Bot('тут_ваш_токен')
dp = Dispatcher()


# Команда /start боту
@dp.message_created(Command('start'))
async def hello(event: MessageCreated):
    await event.message.answer(f"Привет из вебхука!")


async def main():
    await dp.handle_webhook(
        bot=bot, 
        host='localhost',
        port=8080,
        log_level='critical' # Можно убрать для подробного логгирования
    )


if __name__ == '__main__':
    asyncio.run(main())
```