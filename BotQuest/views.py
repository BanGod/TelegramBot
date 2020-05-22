from models import database, User, Point
from datetime import date
from config import is_logged_in, players

def create_tables():
    database.connect()
    database.create_tables([User, Point], safe=True)
    database.close()

def signup(username, id):
    is_logged_in = True
    username = username[8:] if len(username) > 8 else "User_" + str(User.select().count())
    players[id] = username
    print(players[id])
    return User.create(username=username, join_date=date.today(), score = 0)

def get_points():
    query = Point.select()
    return query

def add_points(score, id):
    rec = User.select().where(User.username==players[id])
    rec[0].score += score