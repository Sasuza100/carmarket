from aiogram import types, Dispatcher
from aiogram.types import MediaGroup
from create_bot import dp, bot
from functions import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdd(StatesGroup):
    desc_ex = State()
    collect_data_with_car = State()
    send_to_moder = State()




async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_data_create(username, user_id)
    get_user_data(user_id)
    print(get_user_data(user_id))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я хочу продать машину"]
    keyboard.add(*buttons)
    await bot.send_message(message.from_user.id,
                           "Привет, этот бот поможет тебе опубликовать машину в нашем автосалоне", reply_markup=keyboard)




async def temp(message: types.Message, state: None):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Показать пример"]
    keyboard.add(*buttons)
    await bot.send_message(message.from_user.id,
                           "Отлично, тогда ознакомься с примером", reply_markup=keyboard)
    await FSMAdd.desc_ex.set()

async def process_decs_car_ex(message: types.Message, state: FSMContext):
    print('process_decs_car_ex')
    await bot.send_message(message.from_user.id, "Вот для тебя пример описания")
    await message.reply("Теперь загрузи своё объявление")
    await FSMAdd.next()


global album
album = []

async def collect_data_with_car(message: types.Message, state: FSMContext):
    print('collect_data_with_car')
    try:

        async with state.proxy() as data:
            data['photo'] = message.photo[-1].file_id
            print(message.media_group_id)

            print(data)
            album.append({"media" : data['photo'], "type" : "photo"})
            print(album)
            # await message.reply("Спасибо за публикацию")


    except:
        await message.reply("Прикрепи фото")
        dp.register_message_handler(collect_data_with_car, state=FSMAdd.collect_data_with_car)
    finally:
        await bot.send_media_group(message.from_user.id, media=album)
        await FSMAdd.next()




async def process_send_to_moder(message: types.Message, state: FSMContext):
    print('process_send_to_moder')
    user_id = message.from_user.id





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(temp, lambda message: message.text == "Я хочу продать машину", state=None)
    dp.register_message_handler(process_decs_car_ex, lambda message: message.text == "Показать пример", state=FSMAdd.desc_ex)
    dp.register_message_handler(answer_q3,  state=FSMAdd.collect_data_with_car, content_types=['photo'])
    dp.register_message_handler(process_send_to_moder, state=FSMAdd.send_to_moder)

