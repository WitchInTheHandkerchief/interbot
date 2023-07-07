from aiogram.types import Message

from interbot.db.services import save


def save_telegram_id(msg: Message) -> None:
    return save(f"UPDATE users SET telegram_id = {msg.from_user.id} WHERE token = '{msg.text}';")


def save_full_name(msg: Message) -> None:
    return save(f"UPDATE users SET full_name = '{msg.text}' WHERE telegram_id = {msg.from_user.id};")


def save_sponsor(msg: Message) -> None:
    return save(f"INSERT INTO sponsors(instagram, user_added, date_added) "
                f"VALUES('{msg.text}', (SELECT id from users WHERE telegram_id = {msg.from_user.id}), current_date);")
