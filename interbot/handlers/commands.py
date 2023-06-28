from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from interbot.config import dp
from interbot.services.commands_services import start_command, cancel_command, register_command
from interbot.services.messages_services import process_token_message
from interbot.states import Form


@dp.message_handler(commands=['start'])
async def start(msg: Message) -> None:
    await start_command(msg)


@dp.message_handler(state='*', commands=['cancel'])
async def cancel(msg: Message, state: FSMContext) -> None:
    await cancel_command(msg, state)


@dp.message_handler(commands=['register'])
async def register(msg: Message, state: FSMContext) -> None:
    await register_command(msg, state)


def setup(disp: Dispatcher):
    disp.register_inline_handler(start)
    disp.register_inline_handler(cancel)
    disp.register_inline_handler(register)
