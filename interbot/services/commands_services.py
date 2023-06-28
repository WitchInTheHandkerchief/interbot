from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from interbot.db.services import check_user, check_admin
from interbot.states import Form


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


async def cancel_command(msg: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Отмена')


async def register_command(msg: Message, state: FSMContext) -> None:
    is_registered = check_user(msg.from_user.id)
    if is_registered:
        await msg.answer(text='<b>Вы уже зарегистрированы!</b>', parse_mode=ParseMode.HTML)
    else:
        await state.finish()
        await Form.token.set()
        await msg.answer(text='Введите пожалуйста ваш токен', parse_mode=ParseMode.HTML)


async def register_sponsor_command(msg: Message) -> None:
    is_admin = check_admin(msg.from_user.id)
    if is_admin:
        await msg.answer(text='Введите <b>инстаграм</b> обзвоненного спонсора', parse_mode=ParseMode.HTML)
        await Form.sponsor.set()
    else:
        pass

