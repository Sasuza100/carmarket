from aiogram.utils import executor
from create_bot import dp


async def on_startip():
    print('bot online')

from handlers import admin, client

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True)























# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# from functions import *
# TOKEN = "6293812046:AAFpi1usezc85xiNjEmcyMmV9FIB4YzgXVM"
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# # logging.basicConfig(level=logging.DEBUG)
# # logger = logging.getLogger(__name__)
#
#
#
# @dp.message_handler(content_types=['photo'])
# async def handle_photo(message: types.Message):
#     # вот эту переменную сохраняйте в бд
#     id_photo = message.photo[-1].file_id
#     id_photo1 = message.photo[-2].file_id
#     await bot.send_photo(message.chat.id, id_photo)
