from aiogram import Router, F

from keyboards_buttons.bot_main_menu import main_menu, get_back_button

from selected_category import SelectedCategory


router = Router()


async def answer(callback, text: str):

    SelectedCategory.set(callback.data.split("_")[1])

    match SelectedCategory.get():
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
    print(f"selected_category = {SelectedCategory.get()}")

    await callback.answer()


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback):
    SelectedCategory.set(None)
    await main_menu(callback.message, True)
    await callback.answer()
