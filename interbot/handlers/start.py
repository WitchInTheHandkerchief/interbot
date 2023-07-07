from aiogram.types import Message, ParseMode

from interbot.config import dp
from interbot.db.checkers import check_user, check_admin


@dp.message_handler(commands=['start'])
async def start(msg: Message) -> None:
    is_registered = check_user(msg)
    is_admin = check_admin(msg)
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
