from aiogram.client.default import DefaultBotProperties
import aiogram


class MyBot:
    bot = None

    def __new__(cls):
        with open(".env", "r") as f: BOT_API = f.readline().split("=")[1]
        cls.bot = aiogram.Bot(BOT_API, default=DefaultBotProperties(parse_mode="HTML"))
        return cls.bot


my_bot = MyBot()
