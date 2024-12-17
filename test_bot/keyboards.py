from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Средняя игра', callback_data='M')],
        [InlineKeyboardButton(text='Большая игра', callback_data='L')],
        [InlineKeyboardButton(text='Очень большая игра', callback_data='XL')],
        [InlineKeyboardButton(text='Другие варианты', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='https://ya.ru')]
    ]
)
