import config
import telebot
import utils
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["enter"])
def enter(message):
	utils.set_user_in(message.chat.id)
	answers = ["Да", "Пойдем курить", "Куда положить печенье?", "Как принимать матпомощь?"]
	markup = utils.generate_markup(answers)
	bot.send_message(message.chat.id, text="У тебя что-то срочное?", reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
	is_in = utils.check_user_in(message.chat.id)

	if not is_in:
		bot.send_message(message.chat.id, 'Чтобы войти в 646, выберите команду /enter')
	
	else:
		keyboard_hider = types.ReplyKeyboardRemove()
		if message.text == "Да":
			bot.send_message(message.chat.id, "Тогда я курить!", reply_markup=keyboard_hider)
		elif message.text == "Пойдем курить":
			bot.send_message(message.chat.id, "Курить не предлагать, могу не отказаться", reply_markup=keyboard_hider)
		elif message.text == "Куда положить печенье?":
			bot.send_message(message.chat.id, "*Открывает рот*", reply_markup=keyboard_hider)
		elif message.text == "Как принимать матпомощь?":
			bot.send_message(message.chat.id, "*Не обращает внимания*", reply_markup=keyboard_hider)
		else:
			bot.send_message(message.chat.id, "У тебя что-то срочное?")
			return
	
		utils.set_user_out(message.chat.id)

if __name__ == '__main__':
	bot.infinity_polling()