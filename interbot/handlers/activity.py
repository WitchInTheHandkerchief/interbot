from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ParseMode

from interbot.config import dp
from interbot.db.checkers import check_category_if_exists, check_temp_activity
from interbot.db.fetchers import fetch_categories, fetch_activity
from interbot.db.adjusters import save_category_id, save_activity_name, delete_temp_activity, save_activity
from interbot.filters import IsUser, IsNotCommand
from interbot.states import Form


@dp.message_handler(IsUser(), commands=['add_activity'])
async def add_activity(msg: Message) -> None:
    await msg.answer(text='Выберите одну из нижеперечисленных категорий активности', parse_mode=ParseMode.HTML)
    categories = ''
    for category in fetch_categories():
        categories += f"{category[0]} \n"
    await msg.answer(text=categories, parse_mode=ParseMode.HTML)
    await Form.add_activity.set()


@dp.message_handler(IsNotCommand(), state=Form.add_activity, content_types=['text'])
async def process_activity_category(msg: Message, state: FSMContext) -> None:
    if check_category_if_exists(msg):
        await state.finish()
        if check_temp_activity(msg):
            delete_temp_activity(msg)
        save_category_id(msg)
        await msg.answer(text="Введите точное наименование того, что вы сделали\nПример: 'Обзвонил 10 спонсоров'",
                         parse_mode=ParseMode.HTML)
        await Form.activity_name.set()
    else:
        await msg.answer(text="Категория введена неверно", parse_mode=ParseMode.HTML)


@dp.message_handler(IsNotCommand(), state=Form.activity_name, content_types=['text'])
async def process_activity_name(msg: Message, state: FSMContext) -> None:
    await state.finish()
    save_activity_name(msg)
    await msg.answer(text="Введите точное количество выполненного действия\n"
                          "Пример: Если вы обзвонили 10 спонсоров, введите цифру '10'", parse_mode=ParseMode.HTML)
    await Form.activity_quantity.set()


@dp.message_handler(IsNotCommand(), state=Form.activity_quantity, content_types=['text'])
async def process_activity_quantity(msg: Message, state: FSMContext) -> None:
    if msg.text.isdigit():
        await state.finish()
        save_activity(msg)
        await msg.answer(text="Активность сохранена!")
    else:
        await msg.answer(text="Введите число!")


@dp.message_handler(IsUser(), commands=['check_activity'])
async def check_activity(msg: Message) -> None:
    activity_list = fetch_activity(msg)
    output_message = ""
    if activity_list:
        for activity in activity_list:
            output_message += f"{activity[0]}, {str(activity[1])} баллов, {str(activity[2])}\n"
        output_message += f"В общем: {sum([activity[1] for activity in activity_list])} баллов"
        await msg.answer(text=output_message, parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text="Активность отсутствует", parse_mode=ParseMode.HTML)
