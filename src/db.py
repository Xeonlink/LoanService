import peewee
import uuid


db = peewee.SqliteDatabase("./data/data.db")


class BaseModel(peewee.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class Book(BaseModel):
    """A model for a book."""

    id = peewee.UUIDField(null=False, unique=True, primary_key=True, default=uuid.uuid4)
    barcode_id = peewee.CharField(null=False, unique=True)
    title = peewee.CharField(null=False)
    author = peewee.CharField(null=False)
    publisher = peewee.CharField(null=False)
    classification_num = peewee.CharField(null=False)

    @classmethod
    def select_safe(cls):
        try:
            return list[Book](Book.select())
        except:
            result: list[Book] = []
            return result

    @classmethod
    def is_barcode_exist(cls, barcode_id: str) -> bool:
        try:
            Book.get(barcode_id=barcode_id)
            return True
        except:
            return False


class User(BaseModel):
    """A model for a user."""

    id = peewee.UUIDField(null=False, unique=True, primary_key=True, default=uuid.uuid4)
    loan_code = peewee.IntegerField(null=False, unique=True)
    name = peewee.CharField(null=False)
    contact = peewee.CharField(null=False, unique=True)

    @classmethod
    def select_safe(cls):
        try:
            return list[User](User.select())
        except:
            result: list[User] = []
            return result

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

    id = peewee.UUIDField(null=False, unique=True, primary_key=True)
    book_id = peewee.ForeignKeyField(Book, backref="loans")
    user_id = peewee.ForeignKeyField(User, backref="loans")
    loan_date = peewee.DateTimeField(null=False)
    return_date = peewee.DateTimeField(null=False)


def init():
    db.connect()
    db.create_tables([Book, User, Loan])
