from db.foul.FoulMySQL import FoulMySQL as Foul


class IFoul:

    def __init__(self, db):
        self._db = Foul(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_foul(self, id):
        return self._db.get_foul(id)

    def get_all_fouls(self):
        return self._db.get_all_fouls()

    def get_last_month_foul(self):
        return self._db.get_last_month_foul()