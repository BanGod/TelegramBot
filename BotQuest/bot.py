import config
import telebot
import utils
from telebot import types
from utils import bot

# @bot.callback_query_handler(lambda query: query.data.startswith("kbV"))
# def process_callback(query):
# 	bot.answer_callback_query(query.id, text = options[int(query.data[-1])], show_alert = False)
# 	answers = ["Тогда я курить!", "Курить не предлагать, могу не отказаться", "*Открывает рот*", "*Не обращает внимания*"]
# 	bot.send_message(query.message.chat.id, answers[int(query.data[-1])])


# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def check_answer(message):
# 	if not :
# 		bot.send_message(message.chat.id, 'Чтобы войти в 646, выберите команду /enter')
# 	else:
# 		enter(message)


if __name__ == '__main__':
	bot.infinity_polling()