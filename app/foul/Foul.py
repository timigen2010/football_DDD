class Foul:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.foul.add(data)

    def edit(self, id, data):
        return self._dal.foul.edit(id, data)

    def delete(self, id):
        return self._dal.foul.delete(id)
    
    def get_foul(self, id):
        return self._dal.foul.get_foul(id)

    def get_all_fouls(self):
        return self._dal.foul.get_all_fouls()

    def get_last_month_foul(self):
        return self._dal.foul.get_last_month_foul()