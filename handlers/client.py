from aiogram import types, Dispatcher
from create_bot import dp, bot
from functions import *


# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_data_create(username, user_id, False)
    await bot.send_message(message.from_user.id, "Привет, отправь сюда свою машину по примеру, и мы опубликуем ее в канале @...  (пример)")

async def process_add_car(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message()

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
