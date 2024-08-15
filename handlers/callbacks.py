from aiogram.types import CallbackQuery
from aiogram import Router, F

from keyboard.back_button import get_back_button
from keyboard.reply_keyboard import get_reply_keyboard
from keyboard.menu import menu

router = Router()
selected_category = None


async def answer(callback: CallbackQuery, text: str):
    global selected_category
    selected_category = callback.data.split("_")[1] # type: ignore
    await callback.message.edit_text( # type: ignore
                text=text, 
                reply_markup=get_back_button()
    )


@router.callback_query(F.data.startswith("set_"))
async def get_callback(callback: CallbackQuery):

    category = callback.data.split("_")[1] # type: ignore

    match category:
        case "ФИО": 
            await answer(callback, "Введите ФИО")
        case "город": 
            await answer(callback, "Введите название города")
        case "универ": 
            await answer(callback, "Введите название учебного заведения")
        case "факультет": 
            await answer(callback, "Введите название факультета/института")
        case "специальность": 
            await answer(callback, "Введите название направления")
        case "финансирование": 
            await answer(callback, "Введите вид финансирования")
            await callback.message.answer("жмакните на одну из кнопок", reply_markup=get_reply_keyboard("финансирование")) # type: ignore
        case "форма обучения":
            await answer(callback, "Введите форму обучения")
            await callback.message.answer("жмакните на одну из кнопок", reply_markup=get_reply_keyboard("форма обучения")) # type: ignore

    await callback.answer()


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery):
    global selected_category
    selected_category = None
    await menu(callback.message, True) # type: ignore
    await callback.answer()
