from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from interbot.db.checkers import check_admin, check_user


class IsAdmin(BoundFilter):
    key = "is_admin"

    async def check(self, msg: Message) -> bool:
        return check_admin(msg)


class IsUser(BoundFilter):
    key = "is_user"

    async def check(self, msg: Message) -> bool:
        return check_user(msg)


class IsNotCommand(BoundFilter):
    key = "is_not_command"

    async def check(self, msg: Message) -> bool:
        return not msg.text.startswith("/")


def setup(dp: Dispatcher) -> None:
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsUser)
    dp.filters_factory.bind(IsNotCommand)
