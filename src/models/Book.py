from peewee import CharField, IntegerField, UUIDField
from ..db import BaseModel


class Book(BaseModel):
    """A model for a book."""

    id = UUIDField(null=False, unique=True, primary_key=True)
    barcode_id = IntegerField(null=False, unique=True)
    title = CharField(null=False)
    author = CharField(null=False)
