from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from interbot.config import dp
from interbot.services.commands_services import start_command, cancel_command, register_command, \
    register_sponsor_command, check_sponsor_command, add_activity_command, check_activity_command


@dp.message_handler(commands=['start'])
async def start(msg: Message) -> None:
    await start_command(msg)


@dp.message_handler(state='*', commands=['cancel'])
async def cancel(msg: Message, state: FSMContext) -> None:
    await cancel_command(msg, state)


@dp.message_handler(commands=['register'])
async def register(msg: Message) -> None:
    await register_command(msg)


@dp.message_handler(commands=['register_sponsor'])
async def register_sponsor(msg: Message) -> None:
    await register_sponsor_command(msg)


@dp.message_handler(commands=['check_sponsor'])
async def check_sponsor(msg: Message) -> None:
    await check_sponsor_command(msg)


@dp.message_handler(commands=['add_activity'])
async def add_activity(msg: Message) -> None:
    await add_activity_command(msg)


@dp.message_handler(commands=['check_activity'])
async def check_activity(msg: Message) -> None:
    await check_activity_command(msg)


def setup(disp: Dispatcher):
    disp.register_inline_handler(start)
    disp.register_inline_handler(cancel)
    disp.register_inline_handler(register)
    disp.register_inline_handler(register_sponsor)
    disp.register_inline_handler(check_sponsor)
    disp.register_inline_handler(add_activity)
