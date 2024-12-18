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

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callback_data='stats')],
        [
            InlineKeyboardButton(text='Блокировка', callback_data='block'),
            InlineKeyboardButton(text='Разблокировка', callback_data='unblock')
        ]
    ]
)