#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import telebot

from config import token

bot = telebot.TeleBot(token, skip_pending=True, threaded=False)

# Ловим команду старта при старте без аргументов (первый старт)
@bot.message_handler(func=lambda message: True, commands=['start'])
def start(message):
    if len(sys.argv) != 1:
        return
    bot.send_message(message.chat.id, "Chat ID now %s binded to notifications" % message.chat.id)
    with open('tmp_id', 'w') as id_buf:
        id_buf.write('%s' % message.chat.id)

    print message.chat.id
    sys.exit()


# Если был передан один аргумент, то возвращаем в чат сообщение
if len(sys.argv) == 2:
    number = sys.argv[1]
    try:
        with open('tmp_id', 'r') as id_buf:
            chat_id = id_buf.read()
        bot.send_message(chat_id, "Incoming message: %s" % number)
        print "OK"
    except:
        print "Error"

# Если аргумента нет, то считаем первым стартом и запускаем в режиме полинга
if len(sys.argv) == 1:
    bot.polling(none_stop=True)
