from mongoengine import fields, Document


class Admin(Document):

    password_hash = fields.StringField()