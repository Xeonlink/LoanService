from typing import Literal
from peewee import (
    SqliteDatabase,
    Model,
    UUIDField,
    IntegerField,
    CharField,
    ForeignKeyField,
    DateTimeField,
)
import uuid


db = SqliteDatabase("./data/data.db")


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class Book(BaseModel):
    """A model for a book."""

    id = UUIDField(null=False, unique=True, primary_key=True, default=uuid.uuid4)
    barcode_id = CharField(null=False, unique=True)
    title = CharField(null=False)
    author = CharField(null=False)
    publisher = CharField(null=False)
    classification_num = CharField(null=False)

    @classmethod
    def is_barcode_exist(cls, barcode_id: str) -> bool:
        try:
            Book.get(barcode_id=barcode_id)
            return True
        except:
            return False


class User(BaseModel):
    """A model for a user."""

    id = UUIDField(null=False, unique=True, primary_key=True, default=uuid.uuid4)
    loan_code = IntegerField(null=False, unique=True)
    name = CharField(null=False)
    contact = CharField(null=False, unique=True)

    @classmethod
    def is_loan_code_exist(cls, loan_code: str) -> bool:
        try:
            User.get(barcode_id=loan_code)
            return True
        except:
            return False

    @classmethod
    def is_contact_exist(cls, contact: str) -> bool:
        try:
            User.get(contact=contact)
            return True
        except:
            return False


class Loan(BaseModel):
    """A model for a loan."""

    id = UUIDField(null=False, unique=True, primary_key=True)
    book_id = ForeignKeyField(Book, backref="loans")
    user_id = ForeignKeyField(User, backref="loans")
    loan_date = DateTimeField(null=False)
    return_date = DateTimeField(null=False)


db.connect()
db.create_tables([Book, User], safe=True)

if __name__ == "__main__":
    Book.create(barcode_id=123, title="The Great Gatsby", author="F. Scott Fitzgerald")
