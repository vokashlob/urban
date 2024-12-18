from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()
products = get_all_products()

kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button5 = KeyboardButton(text='Купить')
button10 = KeyboardButton(text='Регистрация')
kb1.row(button1, button2)
kb1.row(button5)
kb1.row(button10)

kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb2.row(button3, button4)

kb3 = InlineKeyboardMarkup()
button6 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button7 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button8 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button9 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3.row(button6, button7, button8, button9)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, @{message.from_user.username}! Я бот помогающий твоему здоровью', reply_markup=kb1)


@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя латиницей:')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь с таким именем уже существует. Введите другое имя')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите ваш email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    if is_included(data['username']):
        await message.answer('Регистрация прошла успешно', reply_markup=kb1)
    else:
        await message.answer('Наши роботы чем-то заняты, им не до вас. Попробуйте в другой раз', reply_markup=kb1)
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} руб')
        with open(f'images/img{product[0]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n'
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    calories_male = calories + 5
    calories_female = calories - 161
    await message.answer(f'Ваша норма {calories_male} ккал, если вы мужчина и {calories_female} ккал, если вы женщина')
    await state.finish()


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
