from app.position.Position import Position as Position


class IPosition:

    def __init__(self, dal):
        self._dal = Position(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_position(self, id):
        return self._dal.get_position(id)

    def get_all_positions(self):
        return self._dal.get_all_positions()