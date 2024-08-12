from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import Text
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types, F
from os import getenv
import asyncio, logging
import csv

# Логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Получение переменной окружения
BOT_API = getenv("BOT_API")

# Объект бота
bot = Bot(token=BOT_API, default=DefaultBotProperties(parse_mode='HTML'))

# Диспетчер
disp = Dispatcher()

# Создание объекта для записи в csv, создание шапки таблицы
with open("universities.csv", 'r+', encoding="utf-8") as f:
    first_row = ["ФИО", "город", "универ", "факультет", "специальность", "финансирование", "форма обучения"]
    csv_writer = csv.writer(f, delimiter = "|", lineterminator="\n")
    if f.readline() != "|".join(first_row) + "\n":
        csv_writer.writerow(first_row)

# Хэндлер на команду /start, приветствие
@disp.message(F.text, Command("start"))
async def greeting(message: types.Message):
    content = Text(f"Привет, {message.from_user.full_name}!\n"
                   "Выбери категорию")
    await message.answer(**content.as_kwargs())

# Хэндлер на текстовое сообщение
@disp.message(F.text)
async def text_message(message: types.Message):
    await message.reply(message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())