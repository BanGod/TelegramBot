from telebot import types
import views
import telebot
import config

bot = telebot.TeleBot(config.token)

def send_question(number, chat_id):
    markup = generate_markup(config.points[number].right_answer, 
                                config.points[number].wrong_answer, number)
    bot.send_message(chat_id, text=config.points[number].question, reply_markup=markup)

def generate_markup(right, wrong, number):
    markup = types.InlineKeyboardMarkup()

    i = 0
    for item in wrong.split(";"):
        markup.add(types.InlineKeyboardButton(item, callback_data=(str(number) + "0")))
        i += 1
    
    markup.add(types.InlineKeyboardButton(right, callback_data=(str(number) + "1")))

    return markup

@bot.callback_query_handler(lambda query: True)
def process_callback(query):
    bot.answer_callback_query(query.id, text = None, show_alert = False)
    bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id)
    number = int(query.data[-2])
    if (query.data[-1] == "0"):
        bot.send_message(query.message.chat.id, "Неверный ответ. Верный ответ: " + config.points[number].right_answer)
    else:
        views.add_points(config.points[number].score)
        bot.send_message(query.message.chat.id, "Верный ответ. Scored: " + str(config.points[number].score))
    if (number < 2):
        send_question(number + 1, query.message.chat.id)
    else:
        res = views.finish_game()
        bot.send_message(query.message.chat.id, text=res)

@bot.message_handler(commands=["signup"])
def signup(message):
    try:
        views.signup(message.text)
    except:
        bot.send_message(message.chat.id, text="Not unique name. /signup again")
    bot.send_message(message.chat.id, text="Your username: " + config.username)

@bot.message_handler(commands=["game"])
def start_game(message):
    if config.is_logged_in:
        config.points = views.get_points()
        send_question(0, message.chat.id)
    else:
        bot.send_message(message.chat.id, text="You need to /signup first")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def process_text(message):
	bot.send_message(message.chat.id, text=message.text)
    