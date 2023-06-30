from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    token = State()
    name = State()
    sponsor = State()
    check_sponsor = State()
    add_activity = State()
