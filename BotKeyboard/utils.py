from config import shelve_name 
import shelve
from telebot import types

def generate_markup(options):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    for item in options:
        markup.add(item)

    return markup


def set_user_in(chat_id):
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)] = chat_id


def set_user_out(chat_id):
    with shelve.open(shelve_name) as storage:
        del storage[str(chat_id)]

def check_user_in(chat_id):
    with shelve.open(shelve_name) as storage:
        try:
            storage[str(chat_id)]
            return True

        except KeyError:
            return False