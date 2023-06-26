import psycopg2
from aiogram import Bot, Dispatcher
from decouple import config

token = config('TOKEN_API')

bot = Bot(token)

dp = Dispatcher(bot)

conn = psycopg2.connect(
    host=config('HOST'),
    database=config('DB'),
    user=config('USER'),
    password=config('PASSWORD'))

cur = conn.cursor()
