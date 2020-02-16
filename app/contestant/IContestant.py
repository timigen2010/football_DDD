from app.contestant.Contestant import Contestant as Contestant


class IContestant:

    def __init__(self, dal):
        self._dal = Contestant(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_contestant(self, id):
        return self._dal.get_contestant(id)

    def get_all_contestants(self):
        return self._dal.get_all_contestants()

    def get_played_contestants(self):
        return self._dal.get_played_contestants()