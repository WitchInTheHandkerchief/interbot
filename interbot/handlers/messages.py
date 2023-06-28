from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from interbot.config import dp
from interbot.services.messages_services import process_token_message, process_name_message
from interbot.states import Form


@dp.message_handler(state=Form.token)
async def process_token(msg: Message, state: FSMContext) -> None:
    await process_token_message(msg, state)


@dp.message_handler(state=Form.name)
async def process_name(msg: Message, state: FSMContext) -> None:
    await process_name_message(msg, state)


def setup(disp: Dispatcher):
    disp.register_inline_handler(process_token)
    disp.register_inline_handler(process_name)
