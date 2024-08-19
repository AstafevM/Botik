from aiogram import Router, F
from keyboards_buttons.bot_main_menu import main_menu, get_back_button
from selected_category import selected_category_instance
from connection_with_db import connect


router = Router()


async def answer(callback, text: str):

    selected_category_instance.set(callback.data.split("_")[1])

    match selected_category_instance.get():
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
    print(f"selected_category = {selected_category_instance.get()}")

    await callback.answer()


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback):
    selected_category_instance.set(None)
    await main_menu(callback.message, callback.from_user.id, True)
    await callback.answer()


@router.callback_query(F.data == "print")
async def print_data(callback):
    await callback.message.edit_text(
        connect.get_user_data(callback.from_user.id),
        reply_markup=get_back_button()
    )
    await callback.answer()
