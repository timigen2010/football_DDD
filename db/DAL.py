from db.IDb import IDb
from db.country.ICountry import ICountry
from db.city.ICity import ICity
from db.liga.ILiga import ILiga


class DAL:
    def __init__(self):
        self._db = IDb()
        self.country = ICountry(self._db)
        self.city = ICity(self._db)
        self.liga = ILiga(self._db)
