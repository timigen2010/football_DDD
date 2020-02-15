class Participation:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.participation.add(data)

    def edit(self, id, data):
        return self._dal.participation.edit(id, data)

    def delete(self, id):
        return self._dal.participation.delete(id)
    
    def get_participation(self, id):
        return self._dal.participation.get_participation(id)

    def get_all_participations(self):
        return self._dal.participation.get_all_participations()
