import psycopg2
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


def check_token(token: int) -> bool:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE token = {token} AND full_name IS NULL;')
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return bool(result[0])
