from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher

from handlers import commands, callbacks
from handlers.values import value_setter

import asyncio
import logging
# import csv


first_row_of_csv = [
    "user_id", "ФИО", "город", "универ", 
    "факультет", "специальность", "финансирование", "форма обучения"
]

# csv_file = open("universities.csv", 'r+', encoding="utf-8")
# csv_writer = csv.DictWriter(csv_file, fieldnames=first_row_of_csv, delimiter = "|", lineterminator='\n')
# csv_reader = csv.DictReader(csv_file, fieldnames=first_row_of_csv, delimiter = "|", lineterminator='\n')

users_data = dict()


async def main():

    logging.basicConfig(level=logging.INFO)

    with open(".env", 'r') as env: 
        BOT_API = env.readline().split("=")[1]

    bot = Bot(token=BOT_API, default=DefaultBotProperties(parse_mode='HTML'))
    dispatcher = Dispatcher()

    dispatcher.include_routers(commands.router, callbacks.router)
    callbacks.router.include_router(value_setter.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
