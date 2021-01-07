from mongoengine import fields, Document


class Contestant(Document):
    """Contestant model definition."""

    name = fields.StringField()
    age = fields.StringField()
    occupation = fields.StringField()
    location = fields.StringField()
    detail = fields.StringField()
    facts = fields.ListField()
    image = fields.StringField()
    active = fields.BooleanField()
    drafted = fields.BooleanField()
    roses = fields.IntField()
