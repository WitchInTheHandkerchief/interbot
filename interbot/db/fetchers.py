from typing import List

from aiogram.types import Message

from interbot.db.services import fetch_all


def fetch_sponsor(msg: Message) -> List[tuple]:
    return fetch_all(f"SELECT instagram, date_added FROM sponsors WHERE instagram = '{msg.text}';")
