from models import database, User, Point
from datetime import date
import config

def create_tables():
    database.connect()
    database.create_tables([User, Point], safe=True)
    database.close()

def signup(username):
    if config.is_logged_in == False:
        config.username = username[8:] if len(username) > 8 else "User_" + str(User.select().count())
        User.create(username=config.username, join_date=date.today(), score = 0)
        config.is_logged_in = True

def get_points():
    query = Point.select()
    return query

def add_points(score):
    (User.update({User.score: User.score + score}).where(User.username==config.username)).execute()

def finish_game():
    rec = User.select().where(User.username==config.username)
    res = rec[0].username + " scored " + str(rec[0].score)
    config.is_logged_in = False
    return res