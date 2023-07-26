from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from interbot.config import dp
from interbot.db.checkers import check_user, check_token
from interbot.db.adjusters import save_telegram_id, save_full_name
from interbot.filters import IsNotCommand
from interbot.states import Form


@dp.message_handler(commands=['register'])
async def register(msg: Message, state: FSMContext) -> None:
    is_registered = check_user(msg)
    if is_registered:
        await msg.answer(text='<b>Вы уже зарегистрированы!</b>', parse_mode=ParseMode.HTML)
    else:
        await state.finish()
        await Form.token.set()
        await msg.answer(text='Введите пожалуйста ваш токен', parse_mode=ParseMode.HTML)


@dp.message_handler(IsNotCommand(), state=Form.token, content_types=['text'])
async def process_token(msg: Message, state: FSMContext) -> None:
    token_exists = False
    try:
        token_exists = check_token(msg)
    except:
        pass
    if token_exists:
        await state.finish()
        await Form.name.set()
        save_telegram_id(msg)
        await msg.answer(text='Введите пожалуйста ваше ФИО', parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text='Вы ввели <b>неверный</b> токен, попробуйте еще раз', parse_mode=ParseMode.HTML)


@dp.message_handler(IsNotCommand(), state=Form.name, content_types=['text'])
async def process_name(msg: Message, state: FSMContext) -> None:
    await state.finish()
    save_full_name(msg)
    await msg.answer(text='<b>Вы успешно зарегистрировались!</b>', parse_mode=ParseMode.HTML)
