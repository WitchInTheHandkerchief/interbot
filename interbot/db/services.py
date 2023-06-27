import psycopg2
from decouple import config


def check_user(user_id: int) -> bool:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {user_id};')
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if result == 1:
        return True
    else:
        return False


def check_admin(user_id: int) -> bool:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {user_id} AND is_admin = true;')
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if result == 1:
        return True
    else:
        return False
