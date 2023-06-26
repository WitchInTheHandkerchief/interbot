from interbot.config import cur


def check_user(user_id: int) -> bool:
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {user_id};')
    result = cur.fetchone()
    if result == 1:
        return True
    else:
        return False


def check_admin(user_id: int) -> bool:
    cur.execute(f'SELECT COUNT(1) FROM USERS WHERE telegram_id = {user_id} AND is_admin = true;')
    result = cur.fetchone()
    if result == 1:
        return True
    else:
        return False
