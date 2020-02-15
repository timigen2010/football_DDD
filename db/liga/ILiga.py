from db.liga.LigaMySQL import LigaMySQL as Liga


class ILiga:

    def __init__(self, db):
        self._db = Liga(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_liga(self, id):
        return self._db.get_liga(id)

    def get_all_ligas(self):
        return self._db.get_all_ligas()