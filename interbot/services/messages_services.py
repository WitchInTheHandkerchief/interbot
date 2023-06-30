from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from interbot.db.services import save_full_name, save_sponsor, fetch_sponsor, save_activity


async def process_name_message(msg: Message, state: FSMContext) -> None:
    await state.finish()
    save_full_name(msg.text, msg.from_user.id)
    await msg.answer(text='<b>Вы успешно зарегистрировались!</b>', parse_mode=ParseMode.HTML)


async def process_sponsor_message(msg: Message, state: FSMContext) -> None:
    save_sponsor(msg, msg.text)
    await state.finish()
    await msg.answer(text='<b>Обзвон зарегистрирован!</b>', parse_mode=ParseMode.HTML)


async def process_checking_sponsor_message(msg: Message, state: FSMContext) -> None:
    await state.finish()
    call_list = fetch_sponsor(msg.text)
    if call_list:
        for call in call_list:
            await msg.answer(text=f'Спонсор {call[0]} был обзвонен {call[1]}', parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text='Спонсор не был обзвонен', parse_mode=ParseMode.HTML)


async def process_activity_message(msg: Message, state: FSMContext) -> None:
    save_activity(msg.text, msg.from_user.id)
    await state.finish()
    await msg.answer(text='Активность сохранена', parse_mode=ParseMode.HTML)

