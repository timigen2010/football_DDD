from app.foul.Foul import Foul as Foul


class IFoul:

    def __init__(self, dal):
        self._dal = Foul(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_foul(self, id):
        return self._dal.get_foul(id)

    def get_all_fouls(self):
        return self._dal.get_all_fouls()