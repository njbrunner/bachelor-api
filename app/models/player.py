from mongoengine import fields, Document


class Player(Document):

    name = fields.StringField()
    team = fields.ListField()
    draft_position = fields.IntField()
