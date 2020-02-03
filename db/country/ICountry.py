from db.country.CountryMySQL import CountryMySQL as Country


class ICountry:

    def __init__(self, db):
        self._db = Country(db)

    def get_all_countries(self):
        return self._db.get_all_countries()