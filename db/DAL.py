from db.IDb import IDb
from db.country.ICountry import ICountry
from db.city.ICity import ICity


class DAL:
    def __init__(self):
        self._db = IDb()
        self.country = ICountry(self._db)
        self.city = ICity(self._db)
