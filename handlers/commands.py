from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import Router, F

from bot import users_data
from keyboard.menu import menu

router = Router()
need_greeting = True

@router.message(Command("start"), F.text)
async def cmd_start(message: Message):
    global need_greeting

    if need_greeting:
        await message.answer(f"Привет, {message.from_user.full_name}!\n") # type: ignore
        need_greeting = False
        users_data[message.from_user.id] = dict() # type: ignore

    await menu(message, False)


@router.message(Command("print"), F.text)
async def cmd_print(message: Message):
    from bot import users_data
    print(users_data)