# -*- coding: utf-8 -*-

import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def echo(message):
	bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.infinity_polling()