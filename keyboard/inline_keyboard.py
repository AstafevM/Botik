from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, Message


def get_inline_keyboard(message: Message, users_data: dict):
    builder = InlineKeyboardBuilder()
    content = [
        "ФИО", "город", "универ", 
        "факультет", "специальность", "финансирование", 
        "форма обучения"
    ]
    
    for i in range(len(content)):
        if content[i] in users_data[message.from_user.id].keys(): # type: ignore
            content[i] = '✅' + content[i]
        builder.add(
            InlineKeyboardButton(
                text=content[i], 
                callback_data=f"set_{ content[i] if content[i][0] != '✅' else content[i][1:] }"
            )
        )

    builder.adjust(3)
    return builder.as_markup()
