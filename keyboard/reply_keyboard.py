from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def get_reply_keyboard(category: str):
    builder = ReplyKeyboardBuilder()
    content = None

    match category:
        case "финансирование":
            content = ["бюджет", "коммерция"]
        case "форма обучения":
            content = ["очно", "заочно"]

    for txt in content: # type: ignore
        builder.add(KeyboardButton(text=txt))

    builder.adjust(2)

    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)
