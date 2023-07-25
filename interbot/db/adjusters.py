from aiogram.types import Message

from interbot.db.services import adjust, fetch_all


def save_telegram_id(msg: Message) -> None:
    adjust(f"UPDATE users SET telegram_id = {msg.from_user.id} WHERE token = '{msg.text}';")


def save_full_name(msg: Message) -> None:
    adjust(f"UPDATE users SET full_name = '{msg.text}' WHERE telegram_id = {msg.from_user.id};")


def save_sponsor(msg: Message) -> None:
    adjust(f"INSERT INTO sponsors(instagram, user_added, date_added) "
           f"VALUES('{msg.text}', (SELECT id from users WHERE telegram_id = {msg.from_user.id}), current_date);")


def save_category_id(msg: Message) -> None:
    adjust(f"INSERT INTO temp_activity(telegram_id, category_id) VALUES({msg.from_user.id},"
           f"(SELECT id FROM activity_categories WHERE name = '{msg.text}'));")


def save_activity_name(msg: Message) -> None:
    adjust(f"UPDATE temp_activity SET name = '{msg.text}' WHERE telegram_id = {msg.from_user.id};")


def delete_temp_activity(msg: Message) -> None:
    adjust(f"DELETE FROM temp_activity WHERE telegram_id = {msg.from_user.id};")


def save_activity(msg: Message) -> None:
    result = fetch_all(f"SELECT name, category_id FROM temp_activity WHERE telegram_id = {msg.from_user.id};")
    adjust(f"INSERT INTO activity(name, category_id, user_id, points, date_added) VALUES"
           f"('{result[0][0]}', {result[0][1]}, (SELECT id FROM users WHERE telegram_id = {msg.from_user.id}), "
           f"(SELECT (points * {int(msg.text)}) FROM activity_categories WHERE id = {result[0][1]}), current_date);")
    adjust(f"DELETE FROM temp_activity WHERE telegram_id = {msg.from_user.id};")
