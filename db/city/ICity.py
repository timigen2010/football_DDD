from db.city.CityMySQL import CityMySQL as City


class ICity:

    def __init__(self, db):
        self._db = City(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_city(self, id):
        return self._db.get_city(id)

    def get_all_cities(self):
        return self._db.get_all_cities()