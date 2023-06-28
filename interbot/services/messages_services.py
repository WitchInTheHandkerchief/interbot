from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from interbot.db.services import check_token, save_telegram_id, save_full_name
from interbot.states import Form


async def process_token_message(msg: Message, state: FSMContext) -> None:
    token_exists = False
    try:
        token_exists = check_token(msg.text)
    except:
        pass
    if token_exists:
        await state.finish()
        await Form.name.set()
        save_telegram_id(msg.from_user.id, msg.text)
        await msg.answer(text='Введите пожалуйста ваше ФИО', parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text='Вы ввели <b>неверный</b> токен, попробуйте еще раз', parse_mode=ParseMode.HTML)


async def process_name_message(msg: Message, state: FSMContext) -> None:
    await state.finish()
    save_full_name(msg.text, msg.from_user.id)
    await msg.answer(text='<b>Вы успешно зарегистрировались!</b>', parse_mode=ParseMode.HTML)
