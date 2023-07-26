from typing import List

from aiogram.types import Message

from interbot.db.services import fetch_all


def fetch_sponsor(msg: Message) -> List[tuple]:
    return fetch_all(f"SELECT instagram, date_added FROM sponsors WHERE instagram = '{msg.text}';")


def fetch_categories() -> List[tuple]:
    return fetch_all(f"SELECT name FROM activity_categories;")


def fetch_activity(msg: Message) -> List[tuple]:
    return fetch_all(f"SELECT name, points, date_added FROM activity WHERE user_id = "
                     f"(SELECT id FROM users WHERE telegram_id = {msg.from_user.id});")
