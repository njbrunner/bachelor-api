from mongoengine import fields, Document


class Player(Document):

    name = fields.StringField()
    team = fields.ListField()