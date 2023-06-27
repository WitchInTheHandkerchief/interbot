from aiogram import Dispatcher
from aiogram.types import Message

from interbot.config import dp
from interbot.services.commands_services import start_command


@dp.message_handler(commands=['start'])
async def start(msg: Message) -> None:
    await start_command(msg)


def setup(dp: Dispatcher):
    dp.register_inline_handler(start)
