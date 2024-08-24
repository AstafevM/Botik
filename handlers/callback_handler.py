from aiogram import Router, F
from keyboards_buttons.bot_main_menu import main_menu, get_back_button
from connection_with_db import connect


router = Router()


async def answer(callback, text: str):

    connect.add_value_to_db(callback.from_user.id, 'selected_category', text)
    
    match connect.get_selected_category(callback.from_user.id):
        case "формаобучения": 
            text = "форму обучения (очно/заочно)"
        case "финансирование":
            text = "вид финансирования (бюджет/коммерция)"

    await callback.message.edit_text(
        text=f"Введите {text}", 
        reply_markup=get_back_button()
    )


@router.callback_query(F.data.startswith("set_"))
async def get_callback(callback):

    category = callback.data.split("_")[1]

    await answer(callback, category)

    await callback.answer()


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback):
    connect.add_value_to_db(callback.from_user.id, 'selected_category', None)
    await main_menu(callback.message, callback.from_user.id, True)
    await callback.answer()


@router.callback_query(F.data == "print")
async def print_data(callback):
    await callback.message.edit_text(
        connect.get_user_data(callback.from_user.id),
        reply_markup=get_back_button()
    )
    await callback.answer()
