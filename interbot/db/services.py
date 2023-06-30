from typing import List

import psycopg2
from aiogram.types import Message
from decouple import config


def check_user(user_id: int) -> bool:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {user_id} AND full_name IS NOT NULL;')
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return bool(result[0])


def check_admin(user_id: int) -> bool:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {user_id} AND is_admin = true AND full_name IS NOT '
                f'NULL;')
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return bool(result[0])


def save_full_name(full_name: str, telegram_id: int) -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users(full_name, telegram_id) VALUES ('{full_name}', {telegram_id});")
    conn.commit()
    cur.close()
    conn.close()


def save_sponsor(msg: Message, sponsor: str) -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f"INSERT INTO sponsors(instagram, user_added, date_added) "
                f"VALUES('{sponsor}', (SELECT id from users WHERE telegram_id = {msg.from_user.id}), current_date);")
    conn.commit()
    cur.close()
    conn.close()


def fetch_sponsor(sponsor: str) -> List[tuple]:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f"SELECT instagram, date_added FROM sponsors WHERE instagram = '{sponsor}';")
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result


def save_activity(activity: str, telegram_id: int) -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f"INSERT INTO activity(name, user_id) VALUES ('{activity}', (SELECT id FROM users WHERE telegram_id = {telegram_id}));")
    conn.commit()
    cur.close()
    conn.close()


def fetch_activity(telegram_id: int) -> List[tuple]:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM activity WHERE user_id = (SELECT id FROM users WHERE telegram_id = {telegram_id});")
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result
