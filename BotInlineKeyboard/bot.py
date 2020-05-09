import config
import telebot
import utils
from telebot import types

bot = telebot.TeleBot(config.token)

options = ["Да", "Пойдем курить", "Куда положить печенье?", "Как принимать матпомощь?"]
is_in = False

@bot.message_handler(commands=["enter"])
def enter(message):
	global is_in 
	is_in = True
	markup = utils.generate_markup(options)
	bot.send_message(message.chat.id, text="У тебя что-то срочное?", reply_markup=markup)

@bot.callback_query_handler(lambda query: True)
def process_callback(query):
	bot.answer_callback_query(query.id, text = options[int(query.data)], show_alert = False)
	answers = ["Тогда я курить!", "Курить не предлагать, могу не отказаться", "*Открывает рот*", "*Не обращает внимания*"]
	bot.send_message(query.message.chat.id, answers[int(query.data)])


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
	if not is_in:
		bot.send_message(message.chat.id, 'Чтобы войти в 646, выберите команду /enter')
	else:
		enter(message)


if __name__ == '__main__':
	bot.infinity_polling()