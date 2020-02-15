from app.liga.Liga import Liga as Liga


class ILiga:

    def __init__(self, dal):
        self._dal = Liga(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_liga(self, id):
        return self._dal.get_liga(id)

    def get_all_ligas(self):
        return self._dal.get_all_ligas()