from db.position.PositionMySQL import PositionMySQL as Position


class IPosition:

    def __init__(self, db):
        self._db = Position(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_position(self, id):
        return self._db.get_position(id)

    def get_all_positions(self):
        return self._db.get_all_positions()