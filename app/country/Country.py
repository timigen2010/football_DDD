class Country:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        self._dal.country.add(data)

    def edit(self, id, data):
        self._dal.country.edit(id, data)

    def delete(self, id):
        self._dal.country.delete(id)

    def get_all_countries(self):
        return self._dal.country.get_all_countries()
