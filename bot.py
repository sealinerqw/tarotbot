import asyncio
import logging

from aiogram import Bot, Dispatcher

from tarotbot import api_key
from tarotbot.handlers import start, horoscope




logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=api_key.API_TOKEN)
    dispatcher = Dispatcher()

    dispatcher.include_router(start.router)
    dispatcher.include_router(horoscope.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())