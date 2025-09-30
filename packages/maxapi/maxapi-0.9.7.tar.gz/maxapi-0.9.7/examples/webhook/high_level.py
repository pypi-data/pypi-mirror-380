import asyncio
import logging

from maxapi import Bot, Dispatcher
from maxapi.types import MessageCreated

logging.basicConfig(level=logging.INFO)

bot = Bot('тут_ваш_токен')
dp = Dispatcher()


@dp.message_created()
async def handle_message(event: MessageCreated):
    await event.message.answer('Бот работает через вебхук!')


async def main():
    await dp.handle_webhook(
        bot=bot, 
        host='localhost',
        port=8080,
        log_level='critical' # Можно убрать для подробного логгирования
    )


if __name__ == '__main__':
    asyncio.run(main())
