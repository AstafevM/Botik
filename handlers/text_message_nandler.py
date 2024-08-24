from aiogram.utils.formatting import Text
from aiogram.filters import Command
from aiogram import Router, F
from connection_with_db import connect
from keyboards_buttons.bot_main_menu import main_menu


router = Router()
need_greeting = True


@router.message(F.text, Command("start"))
async def cmd_start(message):
    global need_greeting

    connect.add_user_to_db(message.from_user.id)

    if need_greeting:
        await message.answer(**Text("Привет, ", message.from_user.full_name, "!\n").as_kwargs())
        need_greeting = False

    await main_menu(message, message.from_user.id, False)


@router.message(F.text)
async def txt_message(message):
    selected_category = connect.get_selected_category(message.from_user.id)
    if selected_category is not None:
        connect.add_value_to_db(message.from_user.id, selected_category, message.text)
        await main_menu(message, message.from_user.id, False)
