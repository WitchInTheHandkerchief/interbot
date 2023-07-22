from aiogram import Dispatcher

from interbot.handlers.activity import add_activity
from interbot.handlers.cancel import cancel
from interbot.handlers.register import register, process_token, process_name
from interbot.handlers.sponsors import register_sponsor, check_sponsor, process_sponsor, process_check_sponsor
from interbot.handlers.start import start


def setup(dp: Dispatcher):
    dp.register_inline_handler(start)
    dp.register_inline_handler(cancel)
    dp.register_inline_handler(register)
    dp.register_inline_handler(register_sponsor)
    dp.register_inline_handler(check_sponsor)
    dp.register_inline_handler(process_token)
    dp.register_inline_handler(process_name)
    dp.register_inline_handler(process_sponsor)
    dp.register_inline_handler(process_check_sponsor)
    dp.register_inline_handler(add_activity)
