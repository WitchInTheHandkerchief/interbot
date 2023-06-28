from aiogram.utils import executor

from interbot.config import dp
from interbot.handlers import commands, messages
from interbot.utils import init_db

if __name__ == '__main__':
    init_db()
    messages.setup(dp)
    commands.setup(dp)
    executor.start_polling(dp)
