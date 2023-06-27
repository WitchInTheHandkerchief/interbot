from aiogram.types import Message

from interbot.db.services import check_user, check_admin


async def start_command(msg: Message) -> None:
    is_registered = check_user(msg.from_user.id)
    is_admin = check_admin(msg.from_user.id)
    if is_registered and is_admin:
        await msg.answer(text='/check_sponsor - чтобы проверить спонсора<br>'
                        '/register_sponsor - чтобы зарегистрировать обзвон спонсора<br>'
                        '/add_activity - чтобы записать свою активность<br>'
                        '/check_activity - чтобы просмотреть свою активность', parse_mode='HTML')
    elif is_registered and not is_admin:
        await msg.answer(text='/check_sponsor - чтобы проверить спонсора<br>'
                        '/add_activity - чтобы записать свою активность<br>'
                        '/check_activity - чтобы просмотреть свою активность', parse_mode='HTML')
    else:
        await msg.answer(text='Пожалуйста зарегистрируйтесь, введя токен командой /register', parse_mode='HTML')
