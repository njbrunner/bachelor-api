from mongoengine import fields, Document


class Admin(Document):

    password = fields.StringField()