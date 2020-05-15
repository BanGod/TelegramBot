from models import database, User, Point
from datetime import date
# from config import is_logged_in

def create_tables():
    with database:
        database.create_tables([User, Point])

def signup(username):
    # is_logged_in = True
    return User.create(username=username, join_date=date(), score = 0)

def get_points():
    query = Point.select()
    for pet in query:
        print(pet.score, pet.right_answer)
    return Point.select()