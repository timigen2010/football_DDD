from db.country.CountryMySQL import CountryMySQL as Country


class ICountry:

    def __init__(self, db):
        self._db = Country(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_country(self, id):
        return self._db.get_country(id)

    def get_all_countries(self):
        return self._db.get_all_countries()