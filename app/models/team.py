from mongoengine import fields, Document


class Team(Document):

    name = fields.StringField()
    owner = fields.StringField()
    team_members = fields.ListField()
    draft_position = fields.IntField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "name": self.name,
            "owner": self.owner,
            "team_members": [contestant.to_json() for contestant in self.team_members],
            "draft_position": self.draft_position,
        }
