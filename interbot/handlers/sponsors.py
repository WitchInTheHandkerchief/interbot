from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from interbot.config import dp
from interbot.db.fetchers import fetch_sponsor
from interbot.db.adjusters import save_sponsor
from interbot.filters import IsAdmin, IsUser
from interbot.states import Form


@dp.message_handler(IsAdmin(), commands=['register_sponsor'])
async def register_sponsor(msg: Message) -> None:
    await msg.answer(text='Введите <b>инстаграм</b> обзвоненного спонсора', parse_mode=ParseMode.HTML)
    await Form.sponsor.set()


@dp.message_handler(IsUser(), commands=['check_sponsor'])
async def check_sponsor(msg: Message) -> None:
    await Form.check_sponsor.set()
    await msg.answer(text='Введите <b>инстаграм</b> спонсора, которого хотите проверить', parse_mode=ParseMode.HTML)


@dp.message_handler(state=Form.sponsor, content_types=['text'])
async def process_sponsor(msg: Message, state: FSMContext) -> None:
    save_sponsor(msg)
    await state.finish()
    await msg.answer(text='<b>Обзвон зарегистрирован!</b>', parse_mode=ParseMode.HTML)


@dp.message_handler(state=Form.check_sponsor, content_types=['text'])
async def process_check_sponsor(msg: Message, state: FSMContext) -> None:
    await state.finish()
    call_list = fetch_sponsor(msg)
    if call_list:
        for call in call_list:
            await msg.answer(text=f'Спонсор {call[0]} был обзвонен {call[1]}', parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text='Спонсор не был обзвонен', parse_mode=ParseMode.HTML)