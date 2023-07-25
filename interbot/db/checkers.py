from aiogram.types import Message

from interbot.db.services import check


def check_user(msg: Message) -> bool:
    return check(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {msg.from_user.id} AND full_name IS NOT NULL;')


def check_admin(msg: Message) -> bool:
    return check(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {msg.from_user.id} AND is_admin = true '
                 f'AND full_name IS NOT NULL;')


def check_token(msg: Message) -> bool:
    return check(f"SELECT COUNT(1) FROM users WHERE token = '{msg.text}' AND full_name IS NULL;")


def check_category_if_exists(msg: Message) -> bool:
    return check(f"SELECT COUNT(1) FROM activity_categories WHERE name = '{msg.text}';")


def check_temp_activity(msg: Message) -> bool:
    return check(f"SELECT COUNT(1) FROM temp_activity WHERE telegram_id = {msg.from_user.id};")
