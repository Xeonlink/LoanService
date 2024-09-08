from peewee import CharField, IntegerField, UUIDField
from ..db import BaseModel


class User(BaseModel):
    """A model for a user."""

    id = UUIDField(null=False, unique=True, primary_key=True)
    barcode_id = IntegerField(null=False, unique=True)
    name = CharField(null=False, unique=True)
    contact = CharField(null=False, unique=True)
    email = CharField(null=False, unique=True)
