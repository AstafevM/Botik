from aiogram.types import Message
from keyboard.inline_keyboard import get_inline_keyboard


async def menu(message: Message, need_edit: bool):
    from bot import users_data
    if need_edit:
        await message.edit_text(
            "Выбери категорию для заполнения",
            reply_markup=get_inline_keyboard(message, users_data)
        )
    else:
        await message.answer(
            "Выбери категорию для заполнения",
            reply_markup=get_inline_keyboard(message, users_data)
        )