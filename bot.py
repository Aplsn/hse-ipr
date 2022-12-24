import telebot
import config
import random
import asyncio

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


dreamies = ['Mark', 'Renjun', 'Jeno', 'Haechan', 'Jaemin', 'Chenle', 'Jisung', '7dream']
photos = ['Mark.jpeg', 'Renjun.jpeg', 'Jeno.jpeg', 'Haechan.jpeg', 'Jaemin.jpeg', 'Chenle.jpeg', 'Jisung.jpeg',
          'dream.jpeg']
songs = ['Joy', 'Candle Light', 'Candy', 'Hair in the Air']


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/jaeminie.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Bias of the day")
    item2 = types.KeyboardButton("Your favorite winter song?")
    item3 = types.KeyboardButton("Commands")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Welcome, {0.first_name}!\nChoose which one u want!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['end'])
def Goodbye(message):
     bot.send_message(message.chat.id,
                     'Goodbye, {0.first_name}!\nStream <strong><a href="https://www.youtube.com/watch?v=zuoSn3ObMz4">Candy</a></strong>'.format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Bias of the day':
            member = (random.randint(0, 7))
            bot.send_message(message.chat.id, dreamies[member])
            bot.send_photo(message.chat.id, open('static/' + photos[member], 'rb'))
        elif message.text == 'Your favorite winter song?':

            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Joy", callback_data='joy'), types.InlineKeyboardButton("Candle Light", callback_data='cl'))
            markup.add(types.InlineKeyboardButton("Candy", callback_data='candy'), types.InlineKeyboardButton("Hair in the Air", callback_data='hita'))


            bot.send_message(message.chat.id, "What's your fav song?", reply_markup=markup)
        elif message.text == 'Commands':
            bot.send_message(message.chat.id, "/start - begin again\n/end - end convo")
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            name=''
            if call.data == 'joy':
                name = 'Joy!'
                bot.send_message(call.message.chat.id, 'Great choice')
            elif call.data == 'cl':
                name = 'Candle Light!'
                bot.send_message(call.message.chat.id, 'Love the pain')
            elif call.data == 'candy':
                name = 'Candy!'
                bot.send_message(call.message.chat.id, 'Great nostalgia')
            elif call.data == 'hita':
                name = 'Hair in the Air!'
                bot.send_message(call.message.chat.id, 'Iconic collab!')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=name,
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
