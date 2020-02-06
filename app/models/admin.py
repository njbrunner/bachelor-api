from mongoengine import fields, Document


class Admin(Document):

    name = fields.StringField()
    password_hash = fields.StringField()