from app.participation.Participation import Participation as Participation


class IParticipation:

    def __init__(self, dal):
        self._dal = Participation(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_participation(self, id):
        return self._dal.get_participation(id)

    def get_all_participations(self):
        return self._dal.get_all_participations()