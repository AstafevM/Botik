from aiogram import Router, F
from aiogram.types import Message


router = Router()


async def set_value_in_dict(message: Message, category: str):
    from keyboard.menu import menu
    from bot import users_data

    users_data[message.from_user.id][category] = message.text # type: ignore
    await menu(message, False)


@router.message(F.text)
async def txt_message(message: Message):
    from handlers.callbacks import selected_category

    match selected_category:
        case "ФИО":
            await set_value_in_dict(message, "ФИО")
        case "город": 
            await set_value_in_dict(message, "город")
        case "универ": 
            await set_value_in_dict(message, "универ")
        case "факультет": 
            await set_value_in_dict(message, "факультет")
        case "специальность": 
            await set_value_in_dict(message, "специальность")
        case "финансирование": 
            await set_value_in_dict(message, "финансирование")
        case "форма обучения": 
            await set_value_in_dict(message, "форма обучения")
        case _:
            await message.answer("ничего не произошло :(")
