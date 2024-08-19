from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, Message

from connection_with_db import connect


def get_back_button():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Назад", 
            callback_data="back_to_menu"
        )
    )
    return builder.as_markup()


def get_menu_keyboard(message):
    builder = InlineKeyboardBuilder()
    titles = [
        "ФИО", "город", "универ", "факультет", "специальность", "финансирование", "формаобучения"
    ]

    for i in range(len(titles)):

        if i == len(titles) - 1:
            button_text = "форма обучения"
        else:
            button_text = titles[i]

        if connect.is_value_in_db(message.from_user.id, titles[i]):
            button_text = '✅' + button_text

        builder.add(
            InlineKeyboardButton(
                text=button_text, 
                callback_data=f"set_{ titles[i] }"
            )
        )

    builder.adjust(3)
    return builder.as_markup()


async def main_menu(message: Message, need_edit: bool):
    content = "Выбери категорию для заполнения.\n"\
              "Чтобы посмотреть внесённые данные введите команду /print"
    if need_edit:
        await message.edit_text(
            content,
            reply_markup=get_menu_keyboard(message)
        )
    else:
        await message.answer(
            content,
            reply_markup=get_menu_keyboard(message)
        )
