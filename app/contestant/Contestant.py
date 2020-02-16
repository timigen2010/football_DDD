class Contestant:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.contestant.add(data)

    def edit(self, id, data):
        return self._dal.contestant.edit(id, data)

    def delete(self, id):
        return self._dal.contestant.delete(id)
    
    def get_contestant(self, id):
        return self._dal.contestant.get_contestant(id)

    def get_all_contestants(self):
        return self._dal.contestant.get_all_contestants()

    def get_played_contestants(self):
        return self._dal.contestant.get_played_contestants()
