from mongoengine import fields, Document


class Player(Document):

    name = fields.StringField()
    team = fields.ListField()
    draft_position = fields.IntField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "name": self.name,
            "team": [contestant.to_json() for contestant in self.team],
            "draft_position": self.draft_position,
        }
