from telebot import types

def generate_markup(options):
    markup = types.InlineKeyboardMarkup()

    i = 0
    for item in options:
        markup.add(types.InlineKeyboardButton(item, callback_data=("1_" + str(i))))
        i += 1  

    return markup