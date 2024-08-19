from aiogram.utils.formatting import Text
from aiogram.filters import Command
from aiogram import Router, F

from connection_with_db import connect

from keyboards_buttons.bot_main_menu import main_menu, get_back_button

from selected_category import SelectedCategory


router = Router()
need_greeting = True


@router.message(F.text, Command("start"))
async def cmd_start(message):
    global need_greeting

    await connect.add_user_to_db(message.from_user.id)

    if need_greeting:
        await message.answer(**Text("Привет, ", message.from_user.full_name, "!\n").as_kwargs())
        need_greeting = False

    await main_menu(message, False)


@router.message(F.text, Command("print"))
async def cmd_print(message):
    await message.answer(
        text=connect.get_user_data(message.from_user.id),
        reply_markup=get_back_button()
    )


@router.message(F.text)
async def txt_message(message):
    if SelectedCategory.get() is not None:
        await connect.add_value_to_db(message.from_user.id, SelectedCategory.get(), message.text)
        await main_menu(message, False)
        print("ДАННЫЕ ЗАПИСАНЫ")
    else:
        message.reply(text="Ничего не понял, но очень интересно.")
