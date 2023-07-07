from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from interbot.config import dp


@dp.message_handler(state='*', commands=['cancel'])
async def cancel(msg: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Отмена')
