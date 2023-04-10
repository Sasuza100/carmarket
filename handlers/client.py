from aiogram import types, Dispatcher
from create_bot import dp, bot
from functions import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import  State, StatesGroup


class FSMAdd(StatesGroup):
    desc_ex = State()
    add_car_card = State()
    send_to_moder = State()




# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_data_create(username, user_id, False)
    get_user_data(user_id)
    await bot.send_message(message.from_user.id,
                           "Привет, отправь сюда свою машину по примеру, и мы опубликуем ее в канале @...")


async def process_decs_car_ex(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Вот для тебя пример описания")
    await FSMAdd.next()
    await message.reply("Теперь загрузи своё объявление")

async def process_add_car_card(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['photo'] = message.photo.file_id
        data['text'] = message.text
    print(data)
    await bot.send_message(message.from_user.id, "Вот для тебя пример описания")
    await FSMAdd.next()
    await message.reply("Теперь загрузи своё объявление")





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_decs_car_ex, commands=['qwe'], state=FSMAdd.desc_ex)
    dp.register_message_handler(process_add_car_card,  state=FSMAdd.add_car_card)

