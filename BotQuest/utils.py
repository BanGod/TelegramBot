from telebot import types
import views
import telebot
import config

bot = telebot.TeleBot(config.token)

def generate_markup(right, wrong, number):
    markup = types.InlineKeyboardMarkup()

    for item in wrong.split(";"):
        markup.add(types.InlineKeyboardButton(item, callback_data=("Quest" + str(number) + "0")))
    
    markup.add(types.InlineKeyboardButton(right, callback_data=("Quest" + str(number) + "1")))

    return markup

@bot.callback_query_handler(lambda query: query.data.startswith("Quest"))
def process_callback(query):
    bot.answer_callback_query(query.id, text = None, show_alert = False)
    # bot.edit_message_reply_markup(chat_id = query.message.chat.id, message_id = query.message.id, reply_markup = None)
    # answers = ["Тогда я курить!", "Курить не предлагать, могу не отказаться", "*Открывает рот*", "*Не обращает внимания*"]
    number = int(query.data[-2])
    if (query.data[-1] == "0"):
        bot.send_message(query.message.chat.id, "Неверный ответ. Верный ответ: " + config.points[number].right_answer)
    else:
        views.add_points(config.points[number].score, query.message.chat.id)
        bot.send_message(query.message.chat.id, "Верный ответ." + str(config.points[number].score))
    if (number < 2):
        markup = generate_markup(config.points[number + 1].right_answer, 
                                config.points[number + 1].wrong_answer, number + 1)
        bot.send_message(query.message.chat.id, text=config.points[number + 1].question, reply_markup=markup)

@bot.message_handler(commands=["signup"])
def signup(message):
    views.signup(message.text, message.chat.id)

@bot.message_handler(commands=["game"])
def start_game(message):
    config.points = views.get_points()
    markup = generate_markup(config.points[0].right_answer, 
                            config.points[0].wrong_answer, 0)
    bot.send_message(message.chat.id, text=config.points[0].question, reply_markup=markup)

# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def process_text(message):
# 	if reg:
# 		bot.send_message(message.chat.id, 'Чтобы войти в 646, выберите команду /enter')
# 	else:
# 		enter(message)
    