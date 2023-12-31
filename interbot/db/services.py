from typing import Any

import psycopg2
from decouple import config


def fetch_all(query: str) -> Any:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result


def check(query: str) -> bool:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return bool(result[0])


def adjust(query: str) -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
