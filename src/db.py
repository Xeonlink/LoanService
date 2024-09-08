from peewee import SqliteDatabase, Model
from .models.Book import Book
from .models.User import User

db = SqliteDatabase("./data/data.db")


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


db.connect()
db.create_tables([Book, User], safe=True)

if __name__ == "__main__":
    print("This is a module, not a script")
    exit(1)
