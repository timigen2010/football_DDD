from app.country.Country import Country as Country


class ICountry:

    def __init__(self, dal):
        self._dal = Country(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_all_countries(self):
        return self._dal.get_all_countries()