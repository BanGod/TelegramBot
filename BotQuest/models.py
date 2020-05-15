from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField, TextField
from config import DATABASE

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    username = CharField(unique=True)
    join_date = DateField()
    score = IntegerField(0)

class Point(BaseModel):
    score = IntegerField()
    question = TextField()
    wrong_answer = TextField()
    right_answer = TextField()