from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import asyncio
import keyboards as kb
import dataHandler
from ast import literal_eval

bot = Bot(token='8084300712:AAECjR_8MV-PznBhK47E3CBAc34uZc5gv5M')
dp = Dispatcher()

@dp.message(CommandStart())
async def startMessageHandler(message: Message):
    dataHandler.auth(int(message.from_user.id))

    await message.answer('<b>👋 Добро пожаловать!</b>\n\nВзаимодействуйте с ботом с помощью нижних кнопок. Приятных покупок!', reply_markup=kb.menu(), parse_mode='html')

@dp.message(F.text == 'Смотреть товары')
async def showHandler(message: Message):
    await message.answer('<b>Выберите категорию товаров...</b>', reply_markup=kb.categories(), parse_mode='html')

# cart
@dp.message(F.text == 'Корзина 🛒')
async def cartHandler(message: Message):
    cart = dataHandler.return_cart(message.from_user.id)
    if str(cart) == '0':
        await message.answer(f'🛒 Ваша корзина пока что пуста...', parse_mode='html')
    else:
        cart = literal_eval(cart)

        positionFullnames = ''
        index = 1
        for position in cart:
            name = dataHandler.return_position_name(position) # Чихуахуа или Лабрадор
            positionFullnames += f'{index}. {name}\n'
            index += 1
            

        await message.answer(f'🛒 <b>Ваша корзина:</b> \n\n{positionFullnames}', parse_mode='html', reply_markup=kb.order())

@dp.callback_query(F.data.startswith('back'))
async def backMenu(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer('<b>Выберите категорию товаров...</b>', reply_markup=kb.categories(), parse_mode='html')

@dp.callback_query(F.data.startswith('dogs'))
async def dogsShow(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer('🐶 <b>Собаки</b>\n\nВыберите интересующую Вас породу...', reply_markup=kb.dogs(), parse_mode='html')

@dp.callback_query(F.data.startswith('cats'))
async def catsShow(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer('🐈 <b>Коты</b>\n\nВыберите интересующую Вас породу...', reply_markup=kb.cats(), parse_mode='html')

@dp.callback_query(F.data.startswith('cucumbers'))
async def cucsShow(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer('🐹 <b>Грызуны</b>\n\nВыберите интересующую Вас породу...', reply_markup=kb.cucu(), parse_mode='html')


# dogs
@dp.callback_query(F.data.startswith('buydog'))
async def buyDog(callback: CallbackQuery):
    index = callback.data[6:]
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    if int(index) == 1:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAID6Gek9IyhZFsPSW7Ezb6dwsUgXB3cAALs9TEbxcIoSRdjP7FW1n_zAQADAgADcwADNgQ', caption=f'Чихуахуа\n\nЧихуахуа — одна из самых маленьких пород собак, но с большим характером. Они преданы своим владельцам и могут быть очень защитными, несмотря на свои скромные размеры. ', reply_markup=kb.addtocart(1))
    if int(index) == 2: 
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAID9Gek9S-6IobfaoZkpegt9sFuJIivAALt9TEbxcIoSfaVoUhDxpvFAQADAgADcwADNgQ', caption=f'Немецкая овчарка\n\nНемецкая овчарка — умная и обучаемая порода, идеальная для службы в полиции и армии. Эти собаки очень преданные и охранительные, что делает их отличными компаньонами. ', reply_markup=kb.addtocart(2))
    if int(index) == 3:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAID9mek9UL8uLn3O36aKYJRYhVCguOjAALv9TEbxcIoSYI02RbzIP2tAQADAgADcwADNgQ', caption=f'Лабрадор\n\nЛабрадор — это дружелюбная и энергичная порода, известная своей преданностью и умом. Они отличные семейные собаки и подходят для активных людей. ', reply_markup=kb.addtocart(3))
    if int(index) == 4:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAID-Gek9VOX8VvQDVvMw3sLrK8y-lkMAALw9TEbxcIoSVPMe47aOtlUAQADAgADcwADNgQ', caption=f'Дворняга\n\nДворняга — собака без определенной породы, которая, как правило, обладает уникальным характером и различными качествами. Эти собаки часто более устойчивы к заболеваниям и могут быть очень любящими и верными спутниками.', reply_markup=kb.addtocart(4))
        
# cats
@dp.callback_query(F.data.startswith('buycat'))
async def buyCat(callback: CallbackQuery):
    index = callback.data[6:]
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    if int(index) == 1:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIEBmek9aQWezyGa-uRK2hG9MpcAAHjPgAC8vUxG8XCKEnzmzFEiBuYEwEAAwIAA3MAAzYE', caption=f'Сиамская\n\nСиамская кошка — грациозная и общительная порода, известная своим характерным окрасом и яркими голубыми глазами. Они очень разговорчивы и любят взаимодействовать с людьми, становясь настоящими компаньонами.', reply_markup=kb.addtocart(5))
    if int(index) == 2:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIECGek9bPBCqB54k6Qb46ZD4uXlL3kAALz9TEbxcIoSaLrtEUledfRAQADAgADcwADNgQ', caption=f'Британская\n\nБританская кошка — крупная и мускулистая порода с густой шерстью и круглой головой. Они спокойны и уравновешены, что делает их отличными домашними любимцами.', reply_markup=kb.addtocart(6))
    if int(index) == 3:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIECmek9clTVsp8oU608iVNepv1lp5cAAL09TEbxcIoSc5Q6uIYUjxNAQADAgADcwADNgQ', caption=f'Мейнкун\n\nМейнкун — одна из самых больших пород домашних кошек с длинной шерстью и пушистым хвостом. Они дружелюбные и игривые, обладают хорошим характером и любят проводить время с семьями.', reply_markup=kb.addtocart(7))
    if int(index) == 4:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIEDGek9d6b4JjW6PhJ8Oafu0TuAAE9XgAC9fUxG8XCKEm6y4aBAZ3p-gEAAwIAA3MAAzYE', caption=f'Кот Семён\n\nСемён  — это кот, у которого нет определенной породы, что придает ему уникальный внешний вид и характер. Они могут быть разнообразными по поведению и окрасу, но часто становятся верными и любящими друзьями.', reply_markup=kb.addtocart(8))
        
# cucumbers
@dp.callback_query(F.data.startswith('buycuc'))
async def buyCuc(callback: CallbackQuery):
    index = callback.data[6:]
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    if int(index) == 1:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIEDmek9gW1k55tTYqyQAHQiITYEdlNAAL29TEbxcIoSW-uHR4J4Ii3AQADAgADcwADNgQ', caption=f'Хомяк\n\nХомяк — маленький и милый грызун, известный своим активным образом жизни, особенно ночью. Они требуют небольшого пространства и являются популярными домашними любимцами благодаря своей игривой натуре.', reply_markup=kb.addtocart(9))
    if int(index) == 2:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIEEGek9hBkBlq-hSRnsrAgwo-pM6jIAAL39TEbxcIoSUQ5EHrMBtg0AQADAgADcwADNgQ', caption=f'Выдра\n\nВыдра, хоть и не совсем грызун, интересный и социальный хищник, который часто обитает в водоемах. Они обладают игривым характером и активно взаимодействуют со своим окружением, что делает их увлекательными для наблюдения.', reply_markup=kb.addtocart(10))
    if int(index) == 3:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIEEmek9h0wyAn7_yq9bMlTKKdzSmpAAAL59TEbxcIoSWkpv9us17DHAQADAgADcwADNgQ', caption=f'Кролик\n\nКролик — обаятельный и мягкий грызун, который славится своим дружелюбным и спокойным нравом. Эти животные могут стать отличными компаньонами и требуют регулярной физической активности и внимания.', reply_markup=kb.addtocart(11))
    if int(index) == 4:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAIEFGek9itkgdgbrvKhxbXGGbqVeclHAAL69TEbxcIoSXLO0y4YZCn8AQADAgADcwADNgQ', caption=f'Крыса\n\nКрыса — умный и социальный грызун, обладающий выдающимся интеллектом и хорошими коммуникативными навыками. Они часто становятся замечательными домашними питомцами, умеющими обучаться трюкам и устанавливать крепкие связи с хозяевами.', reply_markup=kb.addtocart(12))

        
# add to cart
@dp.callback_query(F.data.startswith('add'))
async def addtocartHabndler(callback: CallbackQuery):
    position = int(callback.data[3:]) # 3 or 5 or 13
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    #await callback.message.answer(callback.data[3:])
    await callback.message.answer('Товар добавлен в корзину! ✅', reply_markup=kb.check_cart())

    dataHandler.add_to_cart(callback.from_user.id, position)
    
# clear 
@dp.callback_query(F.data.startswith('clear'))
async def clearHandler(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    dataHandler.clear_cart(callback.from_user.id)
    await callback.message.answer('Ваша корзина очищена.')

# order
@dp.callback_query(F.data.startswith('order'))
async def orderHandler(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer('❓ Введите Ваше ФИО...')
    dataHandler.set_waiting_status(callback.from_user.id, 1)

@dp.message(F.photo)
async def handle_photo(message: Message):
    await message.answer(f'Photo id is {message.photo[0].file_id}')


@dp.message()
async def anyHandler(message: Message):
    admin = 940722904
    status_fio = dataHandler.return_status(message.from_user.id, 1)
    status_number = dataHandler.return_status(message.from_user.id, 2)
    status_address = dataHandler.return_status(message.from_user.id, 3)

    if status_fio == '1':
        print('STATUIS FIO', status_fio)
        dataHandler.set_status(message.from_user.id, 1, message.text)
        await bot.delete_message(message.chat.id, message.message_id)
        await bot.delete_message(message.chat.id, message.message_id-1)
        await message.answer('❓ Введите контактный номер телефона...')
        dataHandler.set_waiting_status(message.from_user.id, 2)

    if status_number == '1':
        dataHandler.set_status(message.from_user.id, 2, message.text)
        await bot.delete_message(message.chat.id, message.message_id)
        await bot.delete_message(message.chat.id, message.message_id-1)
        await message.answer('❓ Введите адрес доставки...')
        dataHandler.set_waiting_status(message.from_user.id, 3)

    if status_address == '1':
        dataHandler.set_status(message.from_user.id, 3, message.text)
        await bot.delete_message(message.chat.id, message.message_id)
        await bot.delete_message(message.chat.id, message.message_id-1)

        cart = dataHandler.return_cart(message.from_user.id)
        cart = literal_eval(cart)
        positionFullnames = ''
        index = 1
        for position in cart:
            name = dataHandler.return_position_name(position) # Чихуахуа или Лабрадор
            positionFullnames += f'{index}. {name}\n'
            index += 1
            

        await message.answer(f'Заказ успешно оформлен! ✅\n\n⭐️ ФИО: {dataHandler.return_status(message.from_user.id, 1)}\n☎️ Номер: {dataHandler.return_status(message.from_user.id, 2)}\n📍 Адрес: {dataHandler.return_status(message.from_user.id, 3)}\n\n🛒 Покупки: \n{positionFullnames}')  
        await bot.send_message(940722904, f'Новый заказ! ⚡️\n\n⭐️ ФИО: {dataHandler.return_status(message.from_user.id, 1)}\n☎️ Номер: {dataHandler.return_status(message.from_user.id, 2)}\n📍 Адрес: {dataHandler.return_status(message.from_user.id, 3)}\n\n🛒 Покупки: \n{positionFullnames}')
        dataHandler.clear_cart(message.from_user.id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())