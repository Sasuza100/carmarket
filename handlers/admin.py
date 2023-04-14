from aiogram import types, Dispatcher
from aiogram.types import MediaGroup
from create_bot import dp, bot
from functions import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    moders = State()
    check_moder_state = State()
    send_message_all = State()
    # send_to_moder = State()


async def admin_test(message: types.Message, state: None):
    user_id = message.from_user.id
    rights = get_user_data(user_id)

    if rights[-1] == 1:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Управление модераторами", "Размещение Рекламы", "Статистика", "Сообщение всем"]
        keyboard.add(*buttons)
        await bot.send_message(message.from_user.id, 'Добро пожаловать в Админ панель', reply_markup=keyboard)
        await FSMAdmin.moders.set()


async def moder_control(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    rights = get_user_data(user_id)
    if rights[-1] == 1:
        await bot.send_message(message.from_user.id, "Введите ник Модератора для изменения состояния(вместе с '@')")
        await FSMAdmin.check_moder_state.set()

async def change_moder_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    rights = get_user_data(user_id)
    if rights[-1] == 1:
        print(message.text[1:len(message.text)])
        if get_user_data_by_name(message.text[1:len(message.text)]) == 0:
            update_moder_data(message.text[1:len(message.text)], 1)
            await bot.send_message(user_id, "Выбранный модератор добавлен")
            await state.finish()
        elif get_user_data_by_name(message.text[1:len(message.text)]) == 1:
            update_moder_data(message.text[1:len(message.text)], 0)
            await bot.send_message(user_id, "Выбранный модератор удалён")
            await state.finish()



async def send_all(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    rights = get_user_data(user_id)
    if rights[-1] == 1:
        await FSMAdmin.send_message_all.set()

async def message_for_all(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    rights = get_user_data(user_id)
    if rights[-1] == 1:

        users = get_users_id()
        for row in users:
            try:
                await bot.send_message(row[0], message.text[5:])
            except:
                print(row[0], "- Неактивный пользователь")
        await state.finish()








def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_test, commands=['admin'], state=None)
    dp.register_message_handler(moder_control, lambda message: message.text == "Управление модераторами", state=FSMAdmin.moders)
    dp.register_message_handler(change_moder_state, lambda message: "@" in message.text, state=FSMAdmin.check_moder_state)
    dp.register_message_handler(send_all, lambda message: message.text == "Сообщение всем", state=FSMAdmin.moders)
    dp.register_message_handler(message_for_all, lambda message: "Всем:" in message.text, state=FSMAdmin.send_message_all)

