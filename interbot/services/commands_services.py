from aiogram.types import Message, ParseMode

from interbot.db.services import check_user, check_admin


async def start_command(msg: Message) -> None:
    is_registered = check_user(msg.from_user.id)
    is_admin = check_admin(msg.from_user.id)
    if is_registered and is_admin:
        await msg.answer(text='<b>/check_sponsor</b> - чтобы проверить спонсора'
                        '                  '
                        '<b>/register_sponsor</b> - чтобы зарегистрировать обзвон спонсора'
                        '                                                                                '
                        '<b>/add_activity</b> - чтобы записать свою активность'
                        '                                                           '
                        '<b>/check_activity</b> - чтобы просмотреть свою активность', parse_mode=ParseMode.HTML)
    elif is_registered and not is_admin:
        await msg.answer(text='<b>/check_sponsor</b> - чтобы проверить спонсора'
                        '      '
                        '<b>/add_activity</b> - чтобы записать свою активность'
                        '                 '
                        '<b>/check_activity</b> - чтобы просмотреть свою активность', parse_mode=ParseMode.HTML)
    else:
        await msg.answer(text='Пожалуйста зарегистрируйтесь, введя токен командой /register', parse_mode=ParseMode.HTML)
    print(msg.from_user.id)
