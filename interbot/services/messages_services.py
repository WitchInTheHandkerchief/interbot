from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from interbot.db.services import check_token
from interbot.states import Form


async def process_token_message(msg: Message, state: FSMContext) -> None:
    token_exists = False
    try:
        token_exists = check_token(msg.text)
    except:
        pass
    if token_exists:
        await Form.name.set()
        await state.finish()
        await msg.answer(text='Введите пожалуйста ваше ФИО', parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text='Вы ввели <b>неверный</b> токен, попробуйте еще раз', parse_mode=ParseMode.HTML)


async def process_name_message(msg: Message, state: FSMContext) -> None:
    pass
