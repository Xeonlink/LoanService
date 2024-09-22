from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    ForeignKeyField,
    DateTimeField,
    IntegerField,
    AutoField,
    BooleanField,
)
from datetime import datetime, timedelta
from constants import DB_PATH


db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    id = AutoField(null=False, unique=True, primary_key=True)
    created_at = DateTimeField(null=False, default=datetime.now)
    updated_at = DateTimeField(null=False, default=datetime.now)

    def save(self, force_insert: bool = False, only=None):
        self.updated_at = datetime.now()
        return super().save(force_insert, only)

    class Meta:
        database = db


class Book(BaseModel):
    """A model for a book."""

    barcode_id = CharField(null=False, unique=True)
    title = CharField(null=False)
    author = CharField(null=False)
    publisher = CharField(null=False)
    classification_num = CharField(null=False)
    is_reading = BooleanField(null=False, default=lambda: False)

    def get_loan(self):
        return self.loan  # type: ignore

    @classmethod
    def safe_get(cls, *query, **filters):
        try:
            return Book.get(*query, **filters)
        except:
            return None

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

    loan_code = IntegerField(null=False, unique=True)
    name = CharField(null=False)
    contact = CharField(null=False, unique=True)

    def save(self, force_insert: bool = False, only=None):
        self.updated_at = datetime.now()
        return super().save(force_insert, only)

    @property
    def can_loan(self) -> bool:
        loans: list[Loan] = list(self.loans)  # type: ignore
        return len(loans) < 5 and all(not loan.is_overdue for loan in loans)

    def get_loans(self):
        return self.loans  # type: ignore

    @property
    def has_overdue(self) -> bool:
        loans: list[Loan] = list(self.loans)  # type: ignore
        return any(loan.return_at is not None and loan.is_overdue for loan in loans)

    @classmethod
    def safe_get(cls, *query, **filters):
        try:
            return User.get(*query, **filters)
        except Exception as e:
            return None

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

    book = ForeignKeyField(Book, backref="loan")
    user = ForeignKeyField(User, backref="loans")
    loan_at = DateTimeField(null=False, default=datetime.now)
    due_at = DateTimeField(null=False)
    return_at = DateTimeField(null=True)

    @classmethod
    def safe_get(cls, *query, **filters):
        try:
            return User.get(*query, **filters)
        except Exception as e:
            print(e)
            return None

    @classmethod
    def select_safe(cls):
        try:
            return list[Loan](Loan.select())
        except:
            result: list[Loan] = []
            return result

    @property
    def is_overdue(self) -> bool:
        return self.due_at < datetime.now()  # type: ignore


def init():
    db.connect()
    db.create_tables([Book, User, Loan])
