class Liga:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.liga.add(data)

    def edit(self, id, data):
        return self._dal.liga.edit(id, data)

    def delete(self, id):
        return self._dal.liga.delete(id)
    
    def get_liga(self, id):
        return self._dal.liga.get_liga(id)

    def get_all_ligas(self):
        return self._dal.liga.get_all_ligas()
