from db.participation.ParticipationMySQL import ParticipationMySQL as Participation


class IParticipation:

    def __init__(self, db):
        self._db = Participation(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_participation(self, id):
        return self._db.get_participation(id)

    def get_all_participations(self):
        return self._db.get_all_participations()