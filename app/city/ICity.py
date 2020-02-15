from app.city.City import City as City


class ICity:

    def __init__(self, dal):
        self._dal = City(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_city(self, id):
        return self._dal.get_city(id)

    def get_all_cities(self):
        return self._dal.get_all_cities()