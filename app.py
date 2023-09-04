import telebot


import Extensions
from Extensions import *

import configurations
from configurations import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])                       # Обработчик команд: start, help
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, text=info_string)


@bot.message_handler(commands=['values'])                               # Обработчик команд: values
def handle_values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key, value in KEY1.items():
        text = '\n'.join((text, f' {key} : {value}', ))
    bot.send_message(message.chat.id, text=text)


@bot.message_handler(content_types=['text', ])                          # Обработчик запросов котировок
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConverterError('Неправильное количество введеных аргументов')

        base, quote, amount = values
        total_base = CurrencyConverter.convert(base, quote, amount)
    except ConverterError as e:
        bot.reply_to(message, f'Ошибка пользователя {e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка обработки {e}')
    else:
        text = f'{amount} {base} это {total_base} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)




