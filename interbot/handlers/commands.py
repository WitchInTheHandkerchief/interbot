from aiogram import Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import Message

from interbot.config import dp
from interbot.services.commands_services import start_command


@dp.message_handler(filters.CommandStart)
async def start(msg: Message) -> None:
    await start_command(msg)


def setup(dp: Dispatcher):
    dp.register_message_handler(start)
