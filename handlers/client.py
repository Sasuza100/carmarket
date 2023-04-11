from aiogram import types, Dispatcher
from aiogram.types import MediaGroup
from create_bot import dp, bot
from functions import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import  State, StatesGroup


class FSMAdd(StatesGroup):
    desc_ex = State()
    collect_data_with_car = State()
    send_to_moder = State()




async def process_start_command(message: types.Message,state: None):
    user_id = message.from_user.id
    username = message.from_user.username
    user_data_create(username, user_id)
    get_user_data(user_id)
    await FSMAdd.desc_ex.set()
    await bot.send_message(message.from_user.id,
                           "Привет, отправь сюда свою машину по примеру, и мы опубликуем ее в канале @...")


async def process_decs_car_ex(message: types.Message, state: FSMContext):
    print('process_decs_car_ex')
    await bot.send_message(message.from_user.id, "Вот для тебя пример описания")
    await message.reply("Теперь загрузи своё объявление")
    await FSMAdd.next()



async def collect_data_with_car(message: types.Message, state: FSMContext):
    print('collect_data_with_car')
    photoes = dict()
    try:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            photoes.append(data['photo'])
            print(photoes)
            await message.reply("Спасибо за публикацию")

            await FSMAdd.next()
    except:
        await message.reply("Прикрепи фото")
        dp.register_message_handler(collect_data_with_car, state=FSMAdd.collect_data_with_car)
    await message.answer_media_group(media=photoes)


async def process_send_to_moder(message: types.Message, state: FSMContext):
    print('process_send_to_moder')
    user_id = message.from_user.id







def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'], state=None)
    dp.register_message_handler(process_decs_car_ex, commands=['qwe'], state=FSMAdd.desc_ex)
    dp.register_message_handler(collect_data_with_car,  state=FSMAdd.collect_data_with_car, content_types=['photo'])
    dp.register_message_handler(process_send_to_moder, state=FSMAdd.send_to_moder)

