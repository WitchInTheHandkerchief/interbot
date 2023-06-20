from aiogram.utils import executor

from interbot.config import dp
from interbot.handlers import messages, commands

if __name__ == '__main__':
    commands.setup(dp)
    messages.setup(dp)
    executor.start_polling(dp)
