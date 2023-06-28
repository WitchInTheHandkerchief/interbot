from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from interbot.config import dp
from interbot.services.messages_services import process_token_message, process_name_message, process_sponsor_message, \
    process_checking_sponsor_message
from interbot.states import Form


@dp.message_handler(state=Form.token, content_types=['text'])
async def process_token(msg: Message, state: FSMContext) -> None:
    await process_token_message(msg, state)


@dp.message_handler(state=Form.name, content_types=['text'])
async def process_name(msg: Message, state: FSMContext) -> None:
    await process_name_message(msg, state)


@dp.message_handler(state=Form.sponsor, content_types=['text'])
async def process_sponsor(msg: Message, state: FSMContext) -> None:
    await process_sponsor_message(msg, state)


@dp.message_handler(state=Form.check_sponsor, content_types=['text'])
async def process_checking_sponsor(msg: Message, state: FSMContext) -> None:
    await process_checking_sponsor_message(msg, state)


def setup(disp: Dispatcher):
    disp.register_inline_handler(process_token)
    disp.register_inline_handler(process_name)
    disp.register_inline_handler(process_sponsor)
    disp.register_inline_handler(process_checking_sponsor)
