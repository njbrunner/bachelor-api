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

    def to_json(self):
        return {
            "_id": str(self.pk),
            "name": self.name,
            "age": self.age,
            "occupation": self.occupation,
            "location": self.location,
            "detail": self.detail,
            "facts": self.facts,
            "image": self.image,
            "active": self.active,
            "drafted": self.drafted,
            "roses": self.roses,
        }
