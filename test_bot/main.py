import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio

from admin import *
from db import *
from config import *
from keyboards import *
import texts


bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def about(message):
    await message.answer(texts.about, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def price(message):
    await message.answer('Что вас интересует?', reply_markup=catalog_kb)


# @dp.callback_query_handler(text='')
# async def buy_(call):
#     await call.message.answer('')
#     await call.answer()


@dp.callback_query_handler(text='M')
async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='L')
async def buy_l(call):
    await call.message.answer(texts.Lgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='XL')
async def buy_xl(call):
    await call.message.answer(texts.XLgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
