from mongoengine import fields, Document


class Player(Document):

    _id = fields.ObjectIdField()
    name = fields.StringField()
    team = fields.ListField()
    draft_position = fields.IntField()
