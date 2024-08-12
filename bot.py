from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from os import getenv

import asyncio
import logging
import csv


async def main():

    logging.basicConfig(level=logging.INFO)

    BOT_API = getenv("BOT_API")

    bot = Bot(token=BOT_API, default=DefaultBotProperties(parse_mode='HTML'))

    dispatcher = Dispatcher()

    f = open("universities.csv", 'r+', encoding="utf-8")
    csv_writer = csv.writer(f, delimiter = "|")
    first_row = ["ФИО", "город", "универ", "факультет", "специальность", "финансирование", "форма обучения"]
    if f.readline() != "|".join(first_row) + "\r\n":
        csv_writer.writerow(first_row)

    await dispatcher.start_polling(bot)
    
    f.close()


if __name__ == "__main__":
    asyncio.run(main())