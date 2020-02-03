from app.country.Country import Country as Country


class ICountry:

    def __init__(self, dal):
        self._dal = Country(dal)

    def get_all_countries(self):
        return self._dal.get_all_countries()