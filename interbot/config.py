from aiogram import Bot, Dispatcher
from decouple import config

token = config('TOKEN_API')

bot = Bot(token)

dp = Dispatcher(bot)
