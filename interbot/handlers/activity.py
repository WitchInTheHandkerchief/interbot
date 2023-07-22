from aiogram.types import Message, ParseMode

from interbot.config import dp
from interbot.db.fetchers import fetch_categories
from interbot.filters import IsUser
from interbot.states import Form


@dp.message_handler(IsUser(), commands=['add_activity'])
async def add_activity(msg: Message) -> None:
    await msg.answer(text='Выберите одну из нижеперечисленных категорий активности', parse_mode=ParseMode.HTML)
    categories = ''
    for category in fetch_categories():
        categories += category[0] + " \n"
    await msg.answer(text=categories, parse_mode=ParseMode.HTML)
    await Form.add_activity.set()


@dp.message_handler(state=Form.add_activity, content_types=['text'])
async def process_add_activity(msg: Message) -> None:
    pass
