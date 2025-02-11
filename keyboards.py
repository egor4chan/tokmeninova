from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def addtocart(position):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add{position}')],
        [InlineKeyboardButton(text='Вернуться назад ◀️', callback_data='back')],
    ])

    return markup

def check_cart():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вернуться назад ◀️', callback_data='back')]
    ])

    return markup

def menu():
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Смотреть товары')],
        [KeyboardButton(text='Корзина 🛒')]
    ], resize_keyboard=True)

    return markup

def categories():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Собаки', callback_data='dogs')],
        [InlineKeyboardButton(text='Коты', callback_data='cats')],
        [InlineKeyboardButton(text='Грызуны', callback_data='cucumbers')]
    ])

    return markup

def dogs():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Чихуахуа', callback_data='buydog1')],
        [InlineKeyboardButton(text='Немецкая овчарка', callback_data='buydog2')],
        [InlineKeyboardButton(text='Лабрадор', callback_data='buydog3')],
        [InlineKeyboardButton(text='Дворняга', callback_data='buydog4')],
        [InlineKeyboardButton(text='Вернуться назад ◀️', callback_data='back')],
        
    ])

    return markup

def cats():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сиамская', callback_data='buycat1')],
        [InlineKeyboardButton(text='Британская', callback_data='buycat2')],
        [InlineKeyboardButton(text='Мейн-кун', callback_data='buycat3')],
        [InlineKeyboardButton(text='Кот Семён', callback_data='buycat4')],
        [InlineKeyboardButton(text='Вернуться назад ◀️', callback_data='back')],
        
    ])

    return markup

def cucu():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Хомяк', callback_data='buycuc1')],
        [InlineKeyboardButton(text='Выдра', callback_data='buycuc2')],
        [InlineKeyboardButton(text='Кролик', callback_data='buycuc3')],
        [InlineKeyboardButton(text='Крыса', callback_data='buycuc4')],
        [InlineKeyboardButton(text='Вернуться назад ◀️', callback_data='back')],
        
    ])

    return markup

def order():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Оформить заказ ⚡️', callback_data='order')],
        [InlineKeyboardButton(text='Очистить корзину', callback_data='clear')]
    ])

    return markup