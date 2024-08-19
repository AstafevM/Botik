from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher

from handlers import callback_handler, text_message_nandler

from bot_instance import my_bot

import logging

import asyncio


async def main():

    logging.basicConfig(level=logging.DEBUG)

    with open(".env", "r") as f: 
        BOT_API = f.readline().split("=")[1]

    bot = Bot(BOT_API, default=DefaultBotProperties(parse_mode="HTML"))

    root_dp = Dispatcher()

    root_dp.include_routers(
        callback_handler.router,
        text_message_nandler.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await root_dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
