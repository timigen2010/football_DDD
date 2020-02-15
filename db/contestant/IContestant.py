from db.contestant.ContestantMySQL import ContestantMySQL as Contestant


class IContestant:

    def __init__(self, db):
        self._db = Contestant(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_contestant(self, id):
        return self._db.get_contestant(id)

    def get_all_contestants(self):
        return self._db.get_all_contestants()