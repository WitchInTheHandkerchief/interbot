from aiogram.utils import executor

from interbot import filters, handlers
from interbot.config import dp
from interbot.utils import init_db

if __name__ == '__main__':
    init_db()
    handlers.setup(dp)
    filters.setup(dp)
    executor.start_polling(dp)
