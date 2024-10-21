import asyncio
import logging

from aiogram import Bot, Dispatcher, types

from tarotbot import api_key
from tarotbot.handlers import start, horoscope


logging.basicConfig(level=logging.INFO)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description="Начать работу с ботом")
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=api_key.API_TOKEN)
    dispatcher = Dispatcher()

    dispatcher.include_router(start.router)
    dispatcher.include_router(horoscope.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, on_startup=set_commands(bot))


if __name__ == '__main__':
    asyncio.run(main())