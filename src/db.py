from peewee import *
import uuid


db = SqliteDatabase("./data/data.db")


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class Book(BaseModel):
    """A model for a book."""

    id = UUIDField(null=False, unique=True, primary_key=True, default=uuid.uuid4)
    barcode_id = IntegerField(null=False, unique=True)
    title = CharField(null=False)
    author = CharField(null=False)


class User(BaseModel):
    """A model for a user."""

    id = UUIDField(null=False, unique=True, primary_key=True)
    barcode_id = IntegerField(null=False, unique=True)
    name = CharField(null=False, unique=True)
    contact = CharField(null=False, unique=True)
    email = CharField(null=False, unique=True)


db.connect()
db.create_tables([Book, User], safe=True)

if __name__ == "__main__":
    Book.create(barcode_id=123, title="The Great Gatsby", author="F. Scott Fitzgerald")
