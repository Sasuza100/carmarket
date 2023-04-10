from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token = '6293812046:AAFpi1usezc85xiNjEmcyMmV9FIB4YzgXVM')
dp = Dispatcher(bot, storage=storage)

