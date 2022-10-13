import logging
import time
from koronaPay import price_koronaPay
from data_garantex import price_garantex
from ipakyulibank import price_ipakyulibank
from binance_price import price_binance
from unistream_price import unistream_price
import telebot
from telebot import TeleBot
import schedule
import random
from logging import basicConfig
import datetime

with open('TOKEN.txt') as f:
    TOKEN = f.read()

token = f"{TOKEN}"

bot = telebot.TeleBot(token)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

print('Run Bot')
#Запсукает функции для отправки и приема данных с бирж
def price():
    return price_koronaPay(), price_garantex(), price_ipakyulibank(), price_binance(), unistream_price()


#красного стакана (сумма) мы вычитаем 0.15%
def calculator(c: str):
    c = float(c)
    a = c*0.15/100
    a = c - a
    a = str(a)
    x = a.split('.')
    new = x[1]
    if len(new) >= 3:
        q = new[:2]
        a = x[0]+'.'+q
        return a

    return a

#Курс 1/0,0057
#Вместо запятой, обязательно точка в текстовом файле!!!!!!!
#Цена берется из текстового документа
def calculator_uz_uzs():
    with open('exchange_rate_for_sending_UZS_from_Russia_to_Uzbekistan.txt') as f:
        rub = f.read()
    sum = str(1/float(rub))
    sum = sum.split('.')
    new_sum = sum[1][:3]
    price = sum[0]+'.'+new_sum
    return price

#якорь #1 из бинанса
def anchor_binance(binance, uz):
    price = str(float(binance)/float(uz))
    price = price.split('.')
    new_price = price[1][:2]
    uzs = price[0]+'.'+new_price
    return uzs


#Высчитываем спред
def spread(korona, binance, garantex, ipabank):
    dollar = 1000*float(ipabank)
    usdt = dollar/float(binance)
    rub = usdt*float(garantex)
    korona_1000 = float(korona)*1000
    spread = korona_1000-rub
    new_spread = str(spread/korona_1000*100)
    sum = new_spread.split('.')
    new_sum = sum[1][:2]
    price = sum[0] + '.' + new_sum
    return price


#Спред Unistream (binance, garantex)
def calculator_unistream(bin, garan, uni):
    anchor = float(bin)/float(uni)
    difference = float(garan) - anchor
    spread = str(difference/anchor*100)
    spread = spread.split('.')
    new_list = spread[1][:3]
    spread = spread[0]+'.'+new_list
    return spread

#Создания инлайн кнопки(Чтобы делать изменения без отправки сообщения)
keyboard = telebot.types.InlineKeyboardMarkup()
button = telebot.types.InlineKeyboardButton(text='', callback_data='start')
keyboard.add(button)

#Отправляет сообщение сразу после запуска бота
@bot.message_handler()
def job(message):
    korona, garantex, ipabank, binance, unistream = price()
    dt = datetime.datetime.now()
    bot.send_message(message.chat.id,
                     f'''🗓️ Обновлено {dt.strftime("%d %B %Y  %H:%M:%S")}\nКурс продажи ₮: {garantex[0]} ₽\nЧистый курс продажи ₮: {calculator(garantex[0])} ₽\nКурс покупки ₮: {garantex[1]} ₽\n
🇺🇿KoronaPay UZ  ₽→$ → : {korona} ₽\n 🇺🇿KoronaPay $: {spread(korona, binance, calculator(garantex[0]), ipabank)}%\n🇺🇿KoronaPay UZ ₽→UZS → : {calculator_uz_uzs()} UZS \n
🇺🇿USDT KoronaPay UZS: {anchor_binance(binance, calculator_uz_uzs())} ₽\n
🟡Unistream ₽→UZS → : {unistream} UZS\n🟡Unistream: {calculator_unistream(binance, calculator(garantex[0]), unistream)}%\nBinance USDT: {binance} UZS\nДля того чтобы обновить нажми /start''', reply_markup=keyboard)
    bot.register_next_step_handler(message = message, function=start(message))

#Основная часть кода
def start(message):
    # Отправляет сообщение раз в (x) промежуток времени
    def xxx(message):
        dt = datetime.datetime.now()
        korona, garantex, ipabank, binance, unistream = price()
        bot.edit_message_text(chat_id=message.chat.id, text=f'''🗓️ Обновлено {dt.strftime("%d %B %Y  %H:%M:%S")}\nКурс продажи ₮: {garantex[0]} ₽\nЧистый курс продажи ₮: {calculator(garantex[0])} ₽\nКурс покупки ₮: {garantex[1]} ₽\n
🇺🇿KoronaPay UZ  ₽→$ → : {korona} ₽\n 🇺🇿KoronaPay $: {spread(korona, binance, calculator(garantex[0]), ipabank)}% \n 🇺🇿KoronaPay UZ ₽→UZS → : {calculator_uz_uzs()} UZS \n
🇺🇿USDT KoronaPay UZS: {anchor_binance(binance, calculator_uz_uzs())} ₽\n
🟡Unistream ₽→UZS → : {unistream} UZS\n 🟡Unistream: {calculator_unistream(binance, calculator(garantex[0]), unistream)}%\nBinance USDT: {binance} UZS\nДля того чтобы обновить нажми /start''',message_id=message.id + 1, reply_markup=keyboard), print("onlain send")



#Отправляет сообщение при спред > 1.1%
    #Сделать time.sleep
    def spread_1_1(message):
        korona, garantex, ipabank, binance, unistream = price()
        new_spread = spread(korona,binance,calculator(garantex[0]), ipabank)
        dt = datetime.datetime.now()
        if float(new_spread) > 0.1:
            bot.send_message(message.chat.id,
                             f'''🗓️ Обновлено {dt.strftime("%d %B %Y  %H:%M:%S")}\nКурс продажи ₮: {garantex[0]} ₽\nЧистый курс продажи ₮: {calculator(garantex[0])} ₽\nКурс покупки ₮: {garantex[1]} ₽\n
🇺🇿KoronaPay UZ  ₽→$ → : {korona} ₽\n🇺🇿KoronaPay $: {spread(korona, binance, calculator(garantex[0]), ipabank)}% \n 🇺🇿KoronaPay UZ ₽→UZS → : {calculator_uz_uzs()} UZS \n
🇺🇿USDT KoronaPay UZS: {anchor_binance(binance, calculator_uz_uzs())} ₽\n
🟡Unistream ₽→UZS → : {unistream} UZS\n 🟡Unistream: {calculator_unistream(binance, calculator(garantex[0]), unistream)}%\nBinance USDT: {binance} UZS\nДля того чтобы обновить нажми /start''',
                             reply_markup=keyboard), print('send message, spread >1.1%')






#Запускается для проверки спреда, если спред >1.1% отправляет сообщение
    schedule.every(15).minutes.do(spread_1_1, message=message)
    #Отпраляет обновление котировок раз в (x) промежуток времени
    schedule.every(25).minutes.do(xxx, message=message)
#Запуск цикла для работы планировщика
    while True:
        schedule.run_pending()
        time.sleep(2)

bot.infinity_polling(skip_pending=True)

























# def start(message):
#     qwe = bot.send_message(-1001744892019, 'Run Bot')
#     schedule.every(1).seconds.do(qwe)
#     while True:
#         schedule.run_pending()
#
#
#
# def job(message):
#     # korona, garantex, ipak = price()
#     # bot.send_message(-1001744892019, f'Корона:{korona},\n Гарантекс: {garantex},\n Ипакбанк:{ipak}' )
#     bot.send_message(-1001744892019, 'While Bot')
# def restart_message():
#     schedule.every(1).seconds.do(job)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

















# storage = MemoryStorage()  # Создание хранилища
# dp = Dispatcher(bot, storage=storage)  # Диспетчер бота
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(filemode='test.log', level=logging.INFO)
# loop = asyncio.get_event_loop()
#
# def price():
#     time.sleep(3)
#     return price_koronaPay(), price_garantex(), price_ipakyulibank()
#
# async def start_price():
#     return await loop.run_in_executor(None, price)
#
# async def message(text):
#     await bot.send_message(915510200, text)
#
#
#
# @dp.message_handler()
# async def main():
#     task1 = asyncio.create_task(price())
#     task2 = asyncio.create_task(message(price()))
#
#     await task1
#     asyncio.sleep(1)
#     await task2
#     await bot.send_message(915510200, f"12")
#
# asyncio.run(main())
# aioschedule.every(15).seconds.do(price)
#
# loop = asyncio.get_event_loop()
# while True:
#     loop.run_until_complete(aioschedule.run_pending())
#
# executor.start_polling(dp, on_startup=on_startup())
